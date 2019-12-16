from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from app01 import myforms
from app01 import models
from django.http import JsonResponse
from django.contrib import auth
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models import F
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
import os
from django.contrib.auth.decorators import login_required

def register(request):
    back_dic = {'code': 100, 'msg': ''}
    form_obj = myforms.RegForm()
    if request.method == 'POST':
        form_obj = myforms.RegForm(request.POST)
        if form_obj.is_valid():
            clean_data = form_obj.cleaned_data
            clean_data.pop('confirm_password')
            avatar = request.FILES.get('myfile')
            if avatar:
                clean_data['avatar'] = avatar
            models.UserInfo.objects.create_user(**clean_data)
            back_dic['msg'] = form_obj.errors
            back_dic['url'] = '/login/'
        else:
            back_dic['msg'] = form_obj.errors
            back_dic['code'] = 101

        return JsonResponse(back_dic)
    return render(request, 'register.html', locals())


def login(request):
    back_dic = {'code': 100, 'msg': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        code = request.POST.get('code')
        if request.session.get('code').upper() == code.upper():
            user_obj = auth.authenticate(request, username=username, password=password)
            if user_obj:
                auth.login(request, user_obj)
                if request.GET.get('next'):
                    back_dic['msg'] = '登录成功'
                    back_dic['url'] = request.GET.get('next')
                    # return redirect(request.GET.get('next'))
                else:
                    back_dic['msg'] = '登录成功'
                    back_dic['url'] = '/home/'
            else:
                back_dic['code'] = 101
                back_dic['msg'] = '用户名或密码错误'
        else:
            back_dic['code'] = 101
            back_dic['msg'] = '验证码错误'
        return JsonResponse(back_dic)

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login/')

from PIL import Image, ImageFont, ImageDraw
from io import BytesIO, StringIO

import random


def get_random():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_code(request):
    io_obj = BytesIO()
    img_obj = Image.new('RGB', (310, 35), get_random())
    draw_obj = ImageDraw.Draw(img_obj)
    font_obj = ImageFont.truetype('static/font/zp.ttf', 40)

    code = ''
    for i in range(5):
        upper_str = str(chr(random.randint(65, 90)))
        lower_str = str(chr(random.randint(95, 122)))
        random_int = str(random.randint(0, 9))
        temp = random.choice([upper_str, lower_str, random_int])
        draw_obj.text((45 + i * 45, -2), temp, get_random(), font_obj)
        code += temp
    print(code)
    request.session['code'] = code
    img_obj.save(io_obj, 'png')
    return HttpResponse(io_obj.getvalue())

# @login_required
def home(request):
    article_list = models.Article.objects.all()
    return render(request, 'home.html', locals())

@login_required
def site(request, username, **kwargs):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        return render(request, 'error.html')
    blog = user_obj.blog
    username = user_obj.username
    article_list = models.Article.objects.filter(blog=blog)
    if kwargs:
        condition = kwargs.get('condition')
        param = kwargs.get('param')
        if condition == 'category':
            article_list = article_list.filter(category_id=param)
        elif condition == 'tag':
            article_list = article_list.filter(tag__id=param)
        else:
            year, month = param.split('-')
            article_list = article_list.filter(create_time__year=year, create_time__month=month)
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c',
                                                                                                       'pk')
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c', 'pk')
    date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values(
        'month').annotate(c=Count('pk')).values_list('month', 'c')

    return render(request, 'site.html', locals())

@login_required
def article_detail(request, username, article_id):
    article_obj = models.Article.objects.filter(pk=article_id).first()
    print(article_obj)
    blog = article_obj.blog.userinfo.blog
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c',
                                                                                                       'pk')
    # print(category_list)

    # 统计当前用户所对应的标签名及标签下的文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c', 'pk')
    # 按照年月分组 统计文章数
    date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values(
        'month').annotate(c=Count('pk')).values_list('month', 'c')
    # print(date_list)
    comment_list = models.Comment.objects.filter(article=article_obj)

    return render(request, 'article_detail.html', locals())


import json


def updown(request):
    """
       点赞点踩业务逻辑
           1.先校验用户是否登录
           2.判断用户是否已经点过了
           3.判断当前文章是否是当前用户自己写的
           4.操作数据库 更新数据
       :param request:
       :return:
       """
    back_dic = {'code': 100, 'msg': ''}
    if request.is_ajax():  # 判断当前请求是否是ajax请求
        article_id = request.POST.get('article_id')
        is_up = request.POST.get('is_up')  # is所对应的布尔值的字符串的形式
        is_up = json.loads(is_up)
        article_obj = models.Article.objects.filter(pk=article_id).first()
        if request.user.is_authenticated():
            is_click = models.UpAndDown.objects.filter(user=request.user, article=article_obj)
            if not is_click:
                if not article_obj.blog.userinfo.username == request.user.username:
                    if is_up:
                        models.Article.objects.filter(pk=article_id).update(up_num=F('up_num') + 1)
                        back_dic['msg'] = '点赞成功'
                    else:
                        models.Article.objects.filter(pk=article_id).update(down_num=F('down_num') + 1)
                        back_dic['msg'] = '点赞成功'
                    models.UpAndDown.objects.create(user=request.user, article=article_obj, is_up=is_up)
                else:
                    back_dic['code'] = 101
                    back_dic['msg'] = '臭不要脸的'
            else:
                back_dic['code'] = 102
                back_dic['msg'] = '已经点过了'
        else:
            back_dic['code'] = 103
            back_dic['msg'] = mark_safe('请先<a href="/login/>登录</a>')

        return JsonResponse(back_dic)


from django.db import transaction


def comment(request):
    back_dic = {'code': 100, 'msg': ""}
    if request.is_ajax():
        article_id = request.POST.get("article_id")
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id")
        with transaction.atomic():
            models.Article.objects.filter(pk=article_id).update(comment_num=F("comment_num") + 1)
            models.Comment.objects.create(user=request.user, article_id=article_id, content=content,
                                          parent_id=parent_id)

        back_dic['msg'] = '评论成功'
    return JsonResponse(back_dic)

@login_required
def backend(request):
    print(request.user)
    article_list = models.Article.objects.filter(blog=request.user.blog)
    return render(request, 'backend/backend.html', locals())

@login_required
def article_delete(request):
    article_id = request.POST.get('id')
    models.Article.objects.filter(pk=article_id).delete()
    print(123)

    return redirect('/backend')


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        soup = BeautifulSoup(content, 'html.parser')
        tags = soup.find_all()
        for tag in tags:
            if tag.name == 'script':
                tag.decompose()  # 如果是script，直接删除
        desc = soup.text[0:150]
        models.Article.objects.create(title=title, content=str(content), desc=desc, blog=request.user.blog)
        return redirect('/backend/')
    return render(request, 'backend/add_article.html')


from myday22BBS import settings


def upload_img(request):
    response_dic = {'error': '', 'url': ''}
    if request.method == 'POST':
        file_obj = request.FILES.get("imgFile")
        if file_obj:
            path = os.path.join(settings.BASE_DIR, 'media', 'article_img')
            if not os.path.exists(path):
                os.mkdir(path)
            file_path = os.path.join(path, file_obj.name)
            with open(file_path, 'wb') as f:
                for line in file_obj:
                    f.write(line)
            response_dic['error'] = 0
            response_dic['url'] = '/media/article_img/%s' % file_obj.name
        else:
            response_dic['error'] = 1
            response_dic['message'] = '文件不存在'

        return JsonResponse(response_dic)

    '''
    //成功时
{
        "error" : 0,
        "url" : "http://www.example.com/path/to/file.ext"
}
//失败时
{
        "error" : 1,
        "message" : "错误信息"
}
    '''
    return HttpResponse('yes')

@login_required
def set_img(request):
    blog = request.user.blog
    username = request.user.username
    if request.method == 'POST':
        file = request.FILES.get('myfile')
        user_obj = models.UserInfo.objects.get(blog=blog)
        user_obj.avatar = file
        user_obj.save()
        # models.UserInfo.objects.filter(blog=blog).update(avatar=file)  # 这种方式修改头像，不回自动在图片前面加avatar前缀 /
        return redirect('/home/')
    return render(request, 'set_img.html')
