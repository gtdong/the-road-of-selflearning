from .project_form import ProjectForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Project
from utils.pagination import Pagination
from django.template.response import TemplateResponse
from utils.git_helper import GitHelper
from utils.ansible_helper import ansible_adhoc_helper


def projectlist(request):
    search = request.GET.get("table_search", "")
    projects = Project.objects.filter(name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), projects.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "projectlist.html", {"projects": projects[pager.start:pager.end], 'page_html': pager.page_html,"page_title":"项目列表",})


def create_project(request,pk=0):
    project = Project.objects.filter(pk=pk).first()
    form = ProjectForm(instance=project)
    if request.method == "POST":
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            GitHelper("/update/git/{}".format(form.cleaned_data["name"])).is_dir(form.cleaned_data["git_path"])
            #创建项目的时候需要创建项目目录
            tasks=[{"action":{"module":"file","args":"path={} state=directory".format(form.cleaned_data["path"])}}]
            ansible_adhoc_helper(form.cleaned_data["server_host"],tasks)
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "project_create.html", {"form": form,"pk":pk})

def del_project(request,pk):
    project=Project.objects.filter(pk=pk).delete()
    print(project)
    return JsonResponse({"status": 0, "msg": "删除成功"})

def detail_project(request,pk):
    project=Project.objects.filter(pk=pk).first()
    return render(request,"project_detail.html",{"project":project})

"""
1.机器上有一个/updata目录
2.目录里面有git和file两个目录
3.git目录放git代码
4.file目录放上传的文件
5.在新建项目的时候，要判断git目录里面是否有项目，如果有的话，则判断是不是git的目录，如果不是，
则需要去git_path clone
6.python操作git
7.gitpython
作业：
1.项目详情页面
1.实现计划任务的增删改查
"""