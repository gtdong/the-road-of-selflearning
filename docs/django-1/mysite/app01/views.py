from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.
def index(request):
    return HttpResponse("Hello django index")

def login(request):
    # print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user_obj = models.User.objects.filter(username=username).first()
        is_exist = models.User.objects.filter(username=username,password=password)
        if is_exist:
            return HttpResponse('登录成功')
        return HttpResponse('登录失败')


    return render(request,'login.html')

def home(request):
    return redirect('https://www.baidu.com')
def user_list(request):
    data = models.User.objects.all()
    print(data)
    # return render(request,'list.html',{'data':data})
    return render(request,'list.html',locals())
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        addr = request.POST.get('addr')
        models.User.objects.create(username=username,password=password,addr=addr)
        # user_obj = models.User()
        # user_obj.username = username
        # user_obj.password = password
        # user_obj.addr = addr
        # user_obj.save()
        return redirect('/user_list')
    return render(request,'register.html')

def edit(request):
    if request.method == 'POST':
        edit_id = request.GET.get('id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        addr = request.POST.get('addr')
        #第一种
        models.User.objects.filter(pk=edit_id).update(username=username,password=password,addr=addr)
        #第二张
        # edit_obj = models.User.objects.filter(pk=edit_id).first()
        # edit_obj.username = username
        # edit_obj.password = password
        # edit_obj.addr = addr
        # edit_obj.save()
        return redirect('/user_list')
    # print(request.GET)
    edit_id = request.GET.get('id')
    edit_obj = models.User.objects.filter(pk=edit_id).first()
    return render(request,'edit.html',locals())

def delete(request):
    delete_id = request.GET.get('id')
    models.User.objects.filter(pk=delete_id).delete() #批量删除

    return redirect('/user_list')