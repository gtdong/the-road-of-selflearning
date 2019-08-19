"""day20 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 无名分组:会将分组内的结果 当做位置参数自动传递给后面的视图函数
    # url(r'^testxxx/',views.test,name='t'),
    # url(r'^test/([0-9]{4})/$',views.test),
    url(r'^test/(\d+)/(?P<id>\d+)/$',views.test,name='ttt'),
    # 有名分组:会将分组内的结果 当做关键字参数自动传递给后面的视图函数
    url(r'^testadd/(?P<id>\d+)/(?P<year>[0-9]{4})/$',views.testadd,name='add'),
    url(r'^home.html',views.home),
    url(r'^index/',views.index),
    # CBV路由配置
    url(r'^login/',views.MyLogin.as_view()),  # url(r'^login/',views.view)

    # 模板语法
    url(r'^demo/',views.demo),

    # 模板的继承与导入
    url(r'^tem/',views.tem),
    url(r'^loginn/',views.loginn),
    url(r'^register/',views.register),



]
# url的第一个参数 其实是一个正则表达式
# 获取用户输入的url 然后根据正则匹配 是否对应
# urls中只要匹配到了 就会立刻执行对应的函数 不会在往下继续匹配
# 第一次如果都没有匹配上的话 会自动加/再次匹配 如果还匹配不上直接报错




