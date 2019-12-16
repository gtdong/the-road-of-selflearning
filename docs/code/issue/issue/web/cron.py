from .cron_form import CronForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Cron
from utils.pagination import Pagination
from django.template.response import TemplateResponse
from utils.ansible_helper import ansible_adhoc_helper

def cronlist(request):
    search = request.GET.get("table_search", "")
    crons = Cron.objects.filter(name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), crons.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "cronlist.html", {"crons": crons[pager.start:pager.end], 'page_html': pager.page_html,"page_title":"计划任务列表",})


def create_cron(request,pk=0):
    cron = Cron.objects.filter(pk=pk).first()
    form = CronForm(instance=cron)
    if request.method == "POST":
        time=request.POST.getlist("time")
        form = CronForm(request.POST, instance=cron)
        if form.is_valid():
            form.instance.time=time
            form.instance.create_user=request.account
            tasks=[{"action":{"module":"cron","args":"minute={} hour={} day={} month={} weekday={} user={} job={} name={}".format(time[0],time[1],time[2],time[3],time[4],form.cleaned_data['user'],form.cleaned_data["job"],form.cleaned_data["name"])}}]
            result=ansible_adhoc_helper(form.cleaned_data["hosts_list"],tasks)
            if not result["ok"]:
                return JsonResponse({"status": 1, "msg": "添加失败"})
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    page_title="新增计划任务" if not pk else "编辑计划任务"
    time=None  if not pk else cron.time
    return render(request, "cron_create.html", {"form": form,"pk":pk,"page_title":page_title,"time":time})

def del_cron(request,pk):
    cron=Cron.objects.filter(pk=pk)
    tasks=[{"action":{"module":'cron',"args":"name={} user={} state=absent".format(cron.first().name,cron.first().user)}}]
    result = ansible_adhoc_helper(cron.first().hosts_list.all(), tasks)
    if not result["ok"]:
        return JsonResponse({"status": 1, "msg": "删除失败"})
    cron.delete()
    return JsonResponse({"status": 0, "msg": "删除成功"})