from django.db.models import Q
from .issue_form import FileForm, GitForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Issue, Host_Issue, Project
from utils.pagination import Pagination
from django.template.response import TemplateResponse
import time, os, random
from utils.git_helper import GitHelper
from utils.ansible_helper import ansible_adhoc_helper
from openpyxl import load_workbook


def updatelist(request):
    search = request.GET.get("table_search", "")
    issues = Issue.objects.filter(Q(user=request.account)|Q(project__test_user=request.account),project__name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), issues.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "updatelist.html",
                            {"issues": issues[pager.start:pager.end], 'page_html': pager.page_html,
                             "page_title": "发布列表" })

def rollbacklist(request):
    search = request.GET.get("table_search", "")
    issues = Issue.objects.filter(Q(user=request.account)|Q(project__test_user=request.account),project__name__contains=search,status="6")
    pager = Pagination(request.GET.get('page', '1'), issues.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "updatelist.html",
                            {"issues": issues[pager.start:pager.end], 'page_html': pager.page_html,
                             "page_title": "回滚列表" })


def handle_uploaded_file(f, t):
    file_list = [file.name for file in f]
    if "readme.xlsx" not in file_list:
        return False
    print(file_list)
    path = "/update/file/{}".format(t)
    if not os.path.exists(path):
        os.makedirs(path)
    for file in f:
        with open("{}/{}".format(path, file.name), 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    return True


def create_file(request):
    form = FileForm()
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        print(request.POST, request.FILES.getlist("file_field"))
        if form.is_valid():
            t = str(int(time.time()))
            form.instance.upload_path = t  # 设置文件上传的路径
            form.instance.backup_path = t
            form.instance.user = request.account  # 设置本次更新的用户
            form.instance.type = "0"  # 设置本次更新的类型
            status = handle_uploaded_file(request.FILES.getlist("file_field"), t)
            if not status:
                return JsonResponse({"status": 1, "msg": "未上传readme.xlsx文件"})
            issue = form.save()
            # 获取当前项目的所有主机
            host_list = form.cleaned_data["project"].server_host.all()
            # 添加到host_issue表中
            for h in host_list:
                Host_Issue.objects.create(project=form.cleaned_data["project"], host=h, issue=issue)
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "file_create.html", {"form": form})


def detail_issue(request, pk):
    issue = Issue.objects.filter(pk=pk).first()
    return render(request, "issue_detail.html", {"issue": issue})


def create_git(request):
    form = GitForm()
    if request.method == "POST":
        print(request.POST)
        form = GitForm(request.POST)
        if form.is_valid():
            t = str(int(time.time()))
            form.instance.upload_path = t  # 设置文件上传的路径
            form.instance.backup_path = t  # 设置备份路径
            form.instance.user = request.account  # 设置本次更新的用户
            form.instance.type = "1"  # 设置本次更新的类型
            issue = form.save()
            if request.POST.get("type") == "tag":
                # 按照tag更新
                GitHelper("/update/git/{}".format(form.cleaned_data["project"].name)).checkout(
                    request.POST.get("commit"), request.POST.get("tag"), "tag")
            else:
                # 基于branch+commit更新
                GitHelper("/update/git/{}".format(form.cleaned_data["project"].name)).checkout(
                    request.POST.get("commit"), request.POST.get("branch"), "bra")
            # 获取当前项目的所有主机
            host_list = form.cleaned_data["project"].server_host.all()
            # 添加到host_issue表中
            for h in host_list:
                Host_Issue.objects.create(project=form.cleaned_data["project"], host=h, issue=issue)
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "git_create.html", {"form": form})


def get_branch(request, pk):
    project = Project.objects.filter(pk=pk).first()
    branches = GitHelper("/update/git/{}".format(project.name)).get_branch()
    return JsonResponse({'data': branches})


def get_commit(request, pk, bra):
    project = Project.objects.filter(pk=pk).first()
    commits = GitHelper("/update/git/{}".format(project.name)).get_commit(bra)
    return JsonResponse({'data': commits})


def get_tag(request, pk):
    project = Project.objects.filter(pk=pk).first()
    tags = GitHelper("/update/git/{}".format(project.name)).get_tags()
    return JsonResponse({'data': tags})


def update(request, pk):
    """
    1.找到所有的机器
    2.从其中随机抽取一台
    3.从nginx上把这台下线
    4.发布
    5.发邮件
    按位与：& 只要有一个0，则为0
    按位或：| 只要有一个为1，则为1
    异或：^ 相等为0，不等为1
    取反：~ -(n+1)
    左移：<<
    右移：>>
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    # 反向查找所有的机器
    issue.status = "1"
    issue.save()
    host_list = issue.host_issue_set.all()
    wait_issue_host = random.choice(host_list)
    print(wait_issue_host)
    # nginx_status=nginx(issue.project,[wait_issue_host],1)
    # server_status=server([wait_issue_host.host],issue)
    nginx_status = True
    server_status = True
    if nginx_status and server_status:
        # 发邮件
        # sendmail()
        issue.status = "2"
        issue.save()
        wait_issue_host.status = "2"
        wait_issue_host.save()
        return JsonResponse({"status": 0, "msg": "成功"})


def nginx(project, wait_host, type):
    print(wait_host)
    """
    在nginx上将主机上线或者下线
    :param nginx_host: nginx的主机
    :param wait_host 需要上线或者下线的机器
    :param type:类型,0 表示上线，1表示下线
    :return:
    """
    tasks = []
    for host in wait_host:
        if type:  # 下线
            tasks.append({"action": {"module": "replace",
                                     "args": "path={} regexp=({}) replace=#\\1".format(project.nginx_conf,
                                                                                       host.host.hostip)},
                          "name": "down"})
        else:  # 上线
            tasks.append({"action": {"module": "replace",
                                     "args": "path={} regexp=#({}) replace=\\1".format(project.nginx_conf,
                                                                                       host.host.hostip)},
                          "name": "down"})
    tasks.append({"action": {"module": "service", "args": "name=nginx state=reloaded"}})
    print(tasks)
    print(project.nginx_host.all())
    result = ansible_adhoc_helper(project.nginx_host.all(), tasks)
    if not result["ok"]:
        return False
    return True


def server(host_list, issue):
    """
    实现主机的发布
    1.备份
    2.将文件复制到远程主机
    :param host_list:
    :return:
    """
    # 先创建目录
    tasks = [{"action": {"module": "file", "args": "path={} state=directory".format("/backup")}}]
    # 将代码备份
    tasks.append(
        {"action": {"module": "shell", "args": "cp -rf {} /backup/{}".format(issue.project.path, issue.backup_path)}})
    if issue.type == "1":  # git更新
        tasks.append({"action": {"module": "copy",
                                 "args": "dest={} src=/update/git/{}/".format(issue.project.path, issue.project.name)}})
    else:  # 文件更新，这个时候需要去获取readme.xlsx文件，依次读取值
        excel_path = "/update/file/{}/readme.xlsx".format(issue.upload_path)
        wb = load_workbook(excel_path)["update"]
        for r in wb.rows:
            tasks.append({"action": {"module": "copy",
                                     "args": "dest={}{} src=/update/file/{}/{}".format(issue.project.path, r[1].value,
                                                                                       issue.upload_path, r[0].value)}})
    print(tasks)
    result = ansible_adhoc_helper(host_list, tasks)
    print(result)
    if not result["ok"]:
        return False
    return True


def success(request, pk):
    """
    测试通过
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    wait_issue_host = issue.host_issue_set.filter(status="2")
    wait_issue_host.update(status="3")
    wait_issue_list = issue.host_issue_set.filter(status="0")
    if wait_issue_list.count() == 0:
        issue.status = "4"
        issue.save()
    else:
        issue.status = "3"
        issue.save()
    # nginx_status = nginx(issue.project, wait_issue_host, 0)

    return JsonResponse({"status": 0, "msg": "成功"})


def again_update(request, pk):
    """
    更新剩余机器
    :param request:
    :param pk:
    :return:
    """
    issue = Issue.objects.filter(pk=pk).first()
    # 反向查找所有的机器
    issue.status = "1"
    issue.save()
    wait_issue_list = issue.host_issue_set.filter(status="0")
    print(wait_issue_list)
    # nginx_status=nginx(issue.project,wait_issue_list,1)
    # #等待更新的机器
    # server_status=server([wait_host.host for wait_host in wait_issue_list],issue)
    nginx_status = True
    server_status = True
    if nginx_status and server_status:
        # 发邮件
        # sendmail()
        issue.status = "2"
        issue.save()
        wait_issue_list.update(status="2")
        return JsonResponse({"status": 0, "msg": "成功"})


def server_rollback(host_list, issue):
    """
    回滚
    :return:
    """
    tasks = [
        {"action": {"module": "shell", "args": "cp -rf /backup/{} {}".format(issue.backup_path, issue.project.path)}}]
    result = ansible_adhoc_helper(host_list, tasks)
    print(result)
    if not result["ok"]:
        return False
    return True


def rollback(request, pk):
    issue = Issue.objects.filter(pk=pk).first()
    host_issue = issue.host_issue_set.filter(Q(status="2") | Q(status="3"))
    # server_rollback([host.host for host in host_issue],issue)
    issue.status = "6"
    issue.save()
    host_issue.update(status="6")
    return JsonResponse({"status": 0, "msg": "成功"})


"""
git更新
1.可以基于branch+commit
2.可以基于tags更新
发布
灰度发布
1.取其中一台机器
2.nginx上摘下来
3.更新（备份）
4.测试（给测试人员发邮件）
5.nginx上线
"""
