from .init_form import InitForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Init
from utils.pagination import Pagination
from django.template.response import TemplateResponse


def initlist(request):
    search = request.GET.get("table_search", "")
    inits = Init.objects.filter(name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), inits.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "initlist.html", {"inits": inits[pager.start:pager.end], 'page_html': pager.page_html,"page_title":"用户列表",})


def create_init(request,pk=0):
    init = Init.objects.filter(pk=pk).first()
    form = InitForm(instance=init)
    if request.method == "POST":
        form = InitForm(request.POST, instance=init)
        if form.is_valid():
            form.instance.create_user=request.account
            # form.cleaned_data['create_user']=request.account
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "init_create.html", {"form": form,"pk":pk})

def del_init(request,pk):
    init=Init.objects.filter(pk=pk).delete()
    return JsonResponse({"status": 0, "msg": "删除成功"})



###需求
"""
1.初始化机器
    ansible api 执行playbook
2.显示当前初始化的详情
    初始化的时间
    初始化的机器
    初始化的人
    初始化的结果
3. 项目管理
    boss字段可以显示user表的所有人
    dev_user 字段只能显示user表中职位是开发的
4. 实现项目的增删改查

"""