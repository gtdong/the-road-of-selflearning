"""issue URL Configuration

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
from web.views import *
from web.user import *
from web.host import *
from web.init import *
from web.initlog import *
from web.project import *
from web.command import *
from web.cron import *
from web.issue import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    # 用户
    url(r'^createuser/', create_user, name='createuser'),
    url(r'^edituser/(\d+)', create_user, name='edituser'),
    url(r'^deluser/(\d+)', del_user, name='deluser'),
    url(r'^userlist/', userlist, name='userlist'),
    # 主机
    url(r'^createhost/', create_host, name='createhost'),
    url(r'^edithost/(\d+)', create_host, name='edithost'),
    url(r'^delhost/(\d+)', del_host, name='delhost'),
    url(r'^hostlist/', hostlist, name='hostlist'),
    # 初始化
    url(r'^createinit/', create_init, name='createinit'),
    url(r'^editinit/(\d+)', create_init, name='editinit'),
    url(r'^delinit/(\d+)', del_init, name='delinit'),
    url(r'^initlist/', initlist, name='initlist'),
    # 初始化机器
    url(r'^createinitlog/', create_initlog, name='createinitlog'),
    url(r'^loglist/(\d+)', loglist, name='loglist'),
    # 项目
    url(r'^createproject/', create_project, name='createproject'),
    url(r'^editproject/(\d+)', create_project, name='editproject'),
    url(r'^delproject/(\d+)', del_project, name='delproject'),
    url(r'^detailproject/(\d+)', detail_project, name='dproject'),
    url(r'^projectlist/', projectlist, name='projectlist'),
    # 命令下发
    url(r'^createcomm/', command_create, name='createcomm'),
    url(r'^commlist/', commandlist, name='commlist'),
    # 计划任务
    url(r'^createcron/', create_cron, name='createcron'),
    url(r'^editcron/(\d+)', create_cron, name='editcron'),
    url(r'^delcron/(\d+)', del_cron, name='delcron'),
    url(r'^cronlist/', cronlist, name='cronlist'),

    # 发布
    url(r'^updatelist/', updatelist, name='updatelist'),
    url(r'^rollbacklist/', rollbacklist, name='rollbacklist'),
    url(r'^fileupdate/', create_file, name='fileupdate'),
    url(r'^gitupdate/', create_git, name='gitupdate'),
    url(r'^detailissue/(\d+)', detail_issue, name='detailissue'),
    url(r'^getbranch/(\d+)', get_branch, name='getbranch'),
    url(r'^gettag/(\d+)', get_tag, name='gettag'),
    url(r'^getcommit/(\d+)/(\w+)', get_commit, name='getcommit'),
    # 更新其中一台
    url(r'^update/(\d+)', update, name='update'),
    # 测试通过
    url(r'^success/(\d+)', success, name='success'),
    # 更新剩余机器
    url(r'^againupdate/(\d+)', again_update, name='againupdate'),
    # 更新剩余机器
    url(r'^rollback/(\d+)', rollback, name='rollback'),
]
