from .host_form import HostForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Host
from utils.pagination import Pagination
from django.template.response import TemplateResponse
from utils.ansible2.runner import AdHocRunner
from utils.ansible2.inventory import Inventory


def hostlist(request):
    search = request.GET.get("table_search", "")
    hosts = Host.objects.filter(name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), hosts.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "hostlist.html", {"hosts": hosts[pager.start:pager.end], 'page_html': pager.page_html,"page_title":"主机列表",})


def create_host(request,pk=0):
    """
    host_data = [
        {
            "hostname": "10.0.0.143",
            "ip": "10.0.0.143",
            "port": 22
        },
    ] #主机列表
    inventory = Inventory(host_data) #动态生成主机配置信息
    runner = AdHocRunner(inventory)
    :param request:
    :param pk:
    :return:
    """
    host = Host.objects.filter(pk=pk).first()
    form = HostForm(instance=host)
    if request.method == "POST":
        print(request.POST)
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            if not host_ping(form.cleaned_data['hostip'],form.cleaned_data['ssh_port']):
                return JsonResponse({"status": 1, "msg": "添加失败，失败原因：主机不可达，请检查网络或者ssh连接"})
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "host_create.html", {"form": form,"pk":pk})

def del_host(request,pk):
    Host.objects.filter(pk=pk).delete()
    return JsonResponse({"status": 0, "msg": "删除成功"})


def host_ping(hostip,ssh_port):
    host_data=[{
        "hostname":hostip,
        "ip":hostip,
        "port":ssh_port
    }]
    inventory = Inventory(host_data)  # 动态生成主机配置信息
    runner = AdHocRunner(inventory)
    tasks=[{
        "action":{"module":'ping'}
    }]
    ret = runner.run(tasks)
    if not ret.results_raw['ok']:
        return False
    return True

