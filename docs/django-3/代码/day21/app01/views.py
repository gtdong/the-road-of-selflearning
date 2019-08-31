from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models
from django.forms import widgets
from django.core.validators import RegexValidator
from functools import wraps
# def login(request):
# #     b_list = []
# #     for i in range(10000):
# #         b_list.append(models.Book(name='第%s本书'%i))
# #     models.Book.objects.bulk_create(b_list)
#
#     queryset = models.Book.objects.all()
#     from app01.utils import mypage
#     current_page = request.GET.get('page',1)
#     all_count = queryset.count()
#     page_obj = mypage.Pagination(current_page=current_page,all_count=all_count,per_page_num=10,pager_count=5)
#     page_queryset = queryset[page_obj.start:page_obj.end]

    # mypage.Pagination()
    # return render(request,'list.html',locals())

from django import forms
# class MyRegForm(forms.Form):
#     name = forms.CharField(max_length=8,label='用户名',initial='张三',error_messages={
#         'max_length':'最大位数为8位',
#         'required':'用户名不能为空'
#     },widget=widgets.TextInput(attrs={'class':'c1'}))
#     password = forms.CharField(max_length=8,min_length=3,
#                                widget=widgets.PasswordInput(attrs={'class':'form-control'}),
#                                validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
#                                            RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
#                                )
#     confirm_password = forms.CharField(max_length=8,min_length=3,
#                                widget=widgets.PasswordInput(attrs={'class':'form-control'}),)
#     email = forms.EmailField(required=False,error_messages={
#         'invalid': '邮箱格式错误'
#     })
#     gender = forms.ChoiceField(
#         choices=((1, "男"), (2, "女"), (3, "保密")),
#         label="性别",
#         initial=3,
#         widget=forms.widgets.RadioSelect()
#     )
#
#     def clean_name(self):
#         name = self.cleaned_data.get('name')
#         if '666' in name:
#             self.add_error('name','光喊666是不行的')
#         return name
#
#     def clean(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if not password == confirm_password:
#             self.add_error('confirm_password','两次密码不一致')
#         return self.cleaned_data
#
# def reg(request):
#     form_obj = MyRegForm()
#     if request.method == 'POST':
#         form_obj = MyRegForm(request.POST)
#         if form_obj.is_valid():
#             return HttpResponse('ok')
#     return render(request,'myform.html',locals())
#
def check_login(func):
    @wraps(func)
    def inner(request,*args,**kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request,*args,**kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner

def login(request):
    if request.method == 'POST':
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if user == "alex" and pwd == "alex1234":
            #设置session
            request.session["user"] = user
            #获取到登录页面之前的URL
            next_url = request.GET.get("next")
            #如果有，就返回跳转之前的URL
            if next_url:
                return redirect(next_url)
            else:
                return redirect("/index/")
    return render(request,"login.html")
@check_login
def logout(request):
    request.session.delete()
    return redirect("/login/")

@check_login
def index(request):
    if request.method == 'POST':
        return redirect("/logout/")
    current_user = request.session.get("user",None)
    return render(request,"index.html",{"user":current_user})
