from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        # 注意  后端获取到的前端提交的数据 默认都是字符串类型
        i1 = request.POST.get('i1')
        i2 = request.POST.get('i2')
        res = int(i1) + int(i2)
        return HttpResponse(res)
    return render(request,'index.html')



def jason(request):
    if request.method == 'POST':
        print(request.POST)  # 针对json格式不做任何处理 不会放到request.POST中
        print(request.FILES)  # 获取前端传输的文件

        # 获取文件对象  你可以直接把它当成 文件句柄   with open(...) as f的那个f
        file_obj = request.FILES.get('myfile')
        print(file_obj.name)  # 查看文件名
        with open(file_obj.name,'wb') as f:
            for line in file_obj:
                f.write(line)
        # print(request.body)  # 原始数据
        # import json
        # res = json.loads(request.body.decode('utf-8'))
        # print(res,type(res))
    return HttpResponse('OK')


from app01 import models
def login(request):
    # for i in range(1000):
    #     models.Book.objects.create(name='第%s本书'%i)
    # b_list = []
    # for i in range(10000):
    #     b_list.append(models.Book(name='第%s本书'%i))
    # models.Book.objects.bulk_create(b_list)  # 批量插入
    # 当前页
    # current_page = request.GET.get('page',1)
    # current_page = int(current_page)
    # # 每页展示的条数
    # per_page_num = 10
    #
    # queryset = models.Book.objects.all()
    # all_count = queryset.count()
    # queryset = models.Book.objects.all()[(current_page - 1) * per_page_num: current_page * per_page_num]
    # page_num, more = divmod(all_count, per_page_num)
    # if more:
    #     page_num += 1
    # page_html = ''
    # for i in range(1,page_num):
    #     res = '<li><a href="?page=%s">%s</a></li>'%(i,i)
    #     page_html += res
    """
    分页器的使用
    只需要获取需要展示的数据

    然后获取总条数 count
    获取当前页面  request.GET.get('page',1)



    :param request:
    :return:
    """
    from app01.urils import mypage
    queryset = models.Book.objects.all()
    current_page = request.GET.get('page',1)
    all_count = queryset.count()
    page_obj = mypage.Pagination(current_page=current_page,all_count=all_count,per_page_num=10,pager_count=5)
    page_queryset = queryset[page_obj.start:page_obj.end]
    return render(request,'list.html',locals())
"""
per_page_num = 10
current_page                   page_start                page_end         
1                               0                           10    
2                               10                          20
3                               20                          30     
4                               30                          40                         

page_start = (current_page-1) * per_page_num
page_end = current_page * per_page_num



数据总共10000
每页展示10条     1000页

数据总共10001
每页展示10条     1001页


页数的获取你可以使用divmod方法
all_count = queryset.count()
per_page_num = 10

page_num,more = divmod(all_count,per_page_num)
if more:
    page_num += 1




"""


from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
class MyRegForm(forms.Form):
    name = forms.CharField(max_length=8,label='用户名',initial="张三",error_messages={
            "max_length":'用户名最大八位',
            'required':"用户名不能为空"
    },widget=widgets.TextInput(attrs={'class':'c1'}))  # name字段最大只能是八位
    password = forms.CharField(max_length=8,min_length=3,
                               widget=widgets.PasswordInput(attrs={'class':'form-control'}),
                               validators=[RegexValidator(r'^[0-9]+$', '请输入数字'),
                                           RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],


                               )  # 最大八位 最少三位
    confirm_password = forms.CharField(max_length=8, min_length=3,
                               widget=widgets.PasswordInput(attrs={'class': 'form-control'})
                               )  # 最大八位 最少三位
    email = forms.EmailField(required=False,error_messages={
        'invalid':'邮箱格式错误'
    })  # email字段接收的数据  必须符合邮箱格式
    gender = forms.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    # 钩子函数
    # 局部钩子  校验单个字段
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if '666' in name:
            self.add_error('name','光喊666是不行的~')
        return name

    # 全局钩子  同时校验多个字段   密码和确认密码
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password','两次密码不一致')
        return self.cleaned_data


def reg(request):
    form_obj = MyRegForm()
    if request.method == 'POST':
        form_obj = MyRegForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('ok')
    return render(request,'myform.html',locals())



def index1(request):
    # obj = HttpResponse('ok')
    # obj.set_cookie('name','jason')  # 设置cookie
    # return obj
    # return HttpResponse('ok')
    #
    # request.session['name'] = 'jason'  # 设置session
    # return HttpResponse('index1')
    print('index1')
    return HttpResponse('ok')
def home(request):
    # if request.COOKIES.get('name'):  # 获取cookie值
    if request.session.get('name'):  # 获取session值
        return HttpResponse('登录成功')
    else:
        return HttpResponse('滚去登录')


def transfer(request):
    if request.method == 'POST':
        print('%s 给 %s 转了 %s'%(request.POST.get('username'),request.POST.get('tran_name'),request.POST.get('money')))
    return render(request,'tran.html')







