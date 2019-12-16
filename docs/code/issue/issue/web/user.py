from .user_form import UserForm
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import UserProfile
from utils.pagination import Pagination
from django.template.response import TemplateResponse


def userlist(request):
    search = request.GET.get("table_search", "")
    users = UserProfile.objects.filter(name__contains=search)
    pager = Pagination(request.GET.get('page', '1'), users.count(), request.GET.copy(), 10)
    return TemplateResponse(request, "userlist.html", {"users": users[pager.start:pager.end], 'page_html': pager.page_html,"page_title":"用户列表",})


def create_user(request,pk=0):
    user = UserProfile.objects.filter(pk=pk).first()
    form = UserForm(instance=user)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": 0, "msg": "添加成功"})
        else:
            return JsonResponse({"status": 1, "msg": "添加失败，失败信息:{}".format(form.errors)})
    return render(request, "user_create.html", {"form": form,"pk":pk})

def del_user(request,pk):
    user=UserProfile.objects.filter(pk=pk).delete()
    print(user)
    return JsonResponse({"status": 0, "msg": "删除成功"})