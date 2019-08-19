from django.shortcuts import render,HttpResponse,redirect,reverse

# Create your views here.
def test(request,*args,**kwargs):
    print(args)
    print(kwargs)
    return HttpResponse('test')


def testadd(request,*args,**kwargs):
    print(args)
    print(kwargs)
    return HttpResponse('testadd')

def home(request):
    # print(reverse('ttt',args=(1,)))
    # # print(reverse('add',args=(1232,)))
    # print(reverse('add',args=(1,3333)))
    # print(reverse('add',kwargs={"id":1234}))
    return render(request,'home.html')

from django.http import JsonResponse
import json

def index(request):
    d = {'name':'jason','password':'123','hobby':'读书'}
    # return HttpResponse(json.dumps(d))
    return JsonResponse(d,json_dumps_params={'ensure_ascii':False})

from django.views import View
class MyLogin(View):
    def get(self,request):
        return HttpResponse('get')

    def post(self,request):
        return HttpResponse('post')


def demo(request):
    i = 1
    f = 1.11
    # s = 'hello'
    s = []
    l = [1,2,3,4,5,6,7,8,9]
    t = (1,2,3,4)
    d = {'name':'jason','password':'123'}
    se = {1,2,3,4}

    n = 23123213342342

    import datetime
    ctime = datetime.datetime.now()
    # sss = 'sajkdj asjdklas askjdklsja sadjklsjadj asjdksa'
    sss = '傻傻的卡死了的。撒娇的空间阿斯加德。萨科dkasjd。'
    """
    1bytes = 8bit
    1024bytes = 1KB
    1024KB = 1MB
    1024MB = 1GB
    1024GB = 1TB
    1024TB = 1PB
    """
    h = "<h1>我是h1标签</h1>"
    s1 = "<script>alert(123)</script>"

    from django.utils.safestring import mark_safe


    s2 =  "<h2>我是h2标签</h2>"
    s2 = mark_safe(s2)


    # s3 = [1,2]
    s3 = [None,1]
    def foo():
        print('foo')
        return '打雷好怕怕'

    class Demo(object):

        def index(self,xxx):
            return 'index'

        @classmethod
        def login(cls):
            return 'cls'

        @staticmethod
        def reg():
            return 'reg'
    obj = Demo()

    # return render(request,'demo.html',{'xxx':[1,2,3,4]})
    return render(request,'demo.html',locals())  # locals会将所在的名称空间中所有的名字全部传递给前端页面



def tem(request):
    return render(request,'tmp.html')


def loginn(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
