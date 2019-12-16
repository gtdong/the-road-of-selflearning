"""myday22BBS URL Configuration

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
from myday22BBS import settings
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^get_code/', views.get_code),
    url(r'^home/', views.home),
    url(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^updown/',views.updown),
    url(r'^comment/',views.comment),
    url(r'^backend/',views.backend),
    url(r'^delete/', views.article_delete),
    url(r'^add_article/', views.add_article),
    url(r'^upload_img/', views.upload_img),
    url(r'^set_img',views.set_img),
    url(r'^logout/',views.logout),
    url(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/',views.article_detail),
    url(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/',views.site),
    url(r'^(?P<username>\w+)/$',views.site),

]
