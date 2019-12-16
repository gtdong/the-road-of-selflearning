from django.http.response import JsonResponse
from .models import Host,Command
from utils.pagination import Pagination
from django.template.response import TemplateResponse
from utils.ansible2.runner import  CommandRunner
from utils.ansible2.inventory import Inventory

def commandlist(request):
    search = request.GET.get("table_search", "")
    if request.account.is_admin=="0":
        comms = Command.objects.filter(command__contains=search)
    else:
        comms = Command.objects.filter(command__contains=search,user=request.account)
    pager = Pagination(request.GET.get('page', '1'), comms.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "commandlist.html",
                            {"comms": comms[pager.start:pager.end], 'page_html': pager.page_html,
                             "page_title": "命令列表", })

def command_create(request):
    host_list=[ {"id": 1, "pId": 0, "name": "主机列表", "open": "true"},]
    for h in Host.objects.all():
        host_list.append({"id": 11, "pId": 1, "name": h.hostip})
    if request.method=="POST":
        hosts=Host.objects.filter(hostip__in=request.POST.getlist("nodes[]"))
        result=command_ansible(hosts,request.POST.get("command"))
        Command.objects.create(hosts_list=request.POST.getlist("nodes[]"),result=result,command=request.POST.get("command"),user=request.account)
        return JsonResponse({"status":0,"msg":result})
    return TemplateResponse(request,'comm_create.html',{"page_title":"创建命令","hosts_list":host_list})

def command_ansible(hostlist,cmd):
    host_data=[{"hostname":h.hostip,"ip":h.hostip,"port":h.ssh_port} for h in hostlist]
    inventory = Inventory(host_data)  # 重新组成虚拟组
    runner = CommandRunner(inventory)
    res = runner.execute(cmd)
    print(res.results_raw)
    return res.results_raw
