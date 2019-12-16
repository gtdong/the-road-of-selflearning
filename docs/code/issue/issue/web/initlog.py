from .initlog_form import InitLogForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import InitLog,Init
from utils.pagination import Pagination
from utils.ansible2.runner import PlayBookRunner
from utils.ansible2.inventory import Inventory

def loglist(request,pk):
    init=Init.objects.filter(pk=pk).first()
    # initlogs=InitLog.objects.filter(init=init) #正向查询
    initlogs=init.initlog_set.all() #反向查询
    pager = Pagination(request.GET.get('page', '1'), initlogs.count(), request.GET.copy(), 2)
    return render(request,"initloglist.html",{"logs": initlogs[pager.start:pager.end], 'page_html': pager.page_html})


def create_initlog(request,pk=0):
    form = InitLogForm()
    if request.method == "POST":
        form = InitLogForm(request.POST)
        if form.is_valid():
            initresult=initlog(form.cleaned_data["hosts_list"],form.cleaned_data["init"].play_book)
            form.instance.result=initresult
            form.instance.user=request.account
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "initlog_create.html", {"form": form,"pk":pk})

def initlog(hostlist,playbook):
    host_data=[{"hostname":h.hostip,"ip":h.hostip,"port":h.ssh_port} for h in hostlist]
    print(host_data)
    inventory = Inventory(host_data)
    runner = PlayBookRunner(inventory).run(playbook)
    return runner