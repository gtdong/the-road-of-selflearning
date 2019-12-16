## 博客园项目

* 需求分析
* 框架，数据库选定
* 项目拆分分组开发
* 测试
* 交付上线

```python
# 项目需求
"""
首页文章展示
文章详情
点赞点踩
文章评论
	-子评论
	-多级评论
注册功能
登陆功能
个人主页
后台管理
	-用户文章展示
	-新增文章
"""

# 数据库表设计
"""
Userinfo表(auth模块)
	-phone手机号
	-create_time注册时间
	-avatar用户头像
	-blog跟Blog表一对一
	
blog表(一个用户对应一个站点,一个用户对应一个特定的主页，即一对一用户表)
	-site_name站点名称
	-site_title站点标题
	-theme站点主题路径
	
Category分类表
	-name分类名称
	-blog个人站点		一对多
	
Tag标签表
	-name标签名称
	-blog个人站点 	一对多
	
Article文章表
	-title文章标题
	-desc文章摘要
	-content文章内容
	-create_time文章发布时间
	外键关系
	-blog文章属于哪个站点		 一对多
	-category文章分类			 一对多
	-tag									多对多

Article2Tag第三章表	
	-article		一对多
	-tag				一对多
	
upanddown点赞点踩表
	-user用户						一对多
	-article文章				一对多
	-is_up点赞或点踩
	
comment评论表
	-user用户							一对多
	-article文章					一对多
	-content评论的内容
  -create_time创建时间
	-parent_id父评论的id 	 自关联
	
关系的判断法则，表里的记录对应关系
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    telephone = models.BigIntegerField(null=True)
    # auto_now_add 创建时自动添加当前时间
    create_date = models.DateField(auto_now_add=True)
    # upload_to需要传一个路径
    # default 默认头像的路径
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.png')
    # 跟Blog表一对一
    blog = models.OneToOneField(to='Blog', to_field='nid',null=True)


class Blog(models.Model):
    site_name = models.CharField(max_length=32)
    site_title = models.CharField(max_length=64)
    # 存css文件的路径
    theme = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=32)
    blog = models.ForeignKey(to='Blog', to_field='nid')


class Tag(models.Model):
    name = models.CharField(max_length=32)
    blog = models.ForeignKey(to='Blog', to_field='nid')


class Article(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    # 存大文本
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    # 跟站点表一对多
    blog = models.ForeignKey(to='Blog', to_field='nid',null=True)
    # 跟分类一对多
    category = models.ForeignKey(to='Category', to_field='nid',null=True)
    # 跟标签多对多,手动创建第三张表
    tag = models.ManyToManyField(to='Tag', through='Article2Tag', through_fields=('article', 'tag'))


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article', to_field='nid')
    tag = models.ForeignKey(to='Tag', to_field='nid')


class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article', to_field='nid')
    is_up = models.BooleanField()


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo')
    article = models.ForeignKey(to='Article', to_field='nid')
    content = models.CharField(max_length=255)
    # 评论时间
    create_time=models.DateTimeField(auto_now_add=True)
    # parent =models.ForeignKey(to='Comment',to_field='nid')
    # 自关联,存父评论id
    parent = models.ForeignKey(to='self', to_field='nid',null=True)
    # parent =models.IntegerField()

```

# BBS项目功能模块

#### 1.注册页面搭建

* forms组件渲染用户名，密码，确认密码，邮箱

  ```html
  <form id="myform" novalidate>
                  {% csrf_token %}
                  {% for foo in form_obj %}
                      {#加一个div样式为form-group，能够增大input框之间的距离#}
                      <div class="form-group">
                          <label for="{{ foo.auto_id }}">{{ foo.label }}</label>
                          {{ foo }}
                          <span class="error pull-right"></span>
                      </div>
                  {% endfor %}
                  <input type="button" value="提交" class="btn btn-primary pull-right" id="id_submit">
              </form>
  ```

* 获取用户头像手动渲染标签，并利用label跳转input特效，实现点击图片选择文件效果

  ```html
  <div class="form-group">
                      <label for="myfile">头像
                          <img src="/static/img/default.png" height="80" alt="" style="margin-left: 20px" id="img">
                      </label>
                      <input type="file" id="myfile" style="display: none">
                  </div>
  ```

* js代码实时展示用户头像

  ```js
  $('#myfile').change(function () {
          // 获取文件对象
          var myfile = $(this)[0].files[0];
          // 生成一个文件阅读器对象
          var filereader = new FileReader();
          // 将文件对象放入文件阅读器中
          filereader.readAsDataURL(myfile);
          // 动态展示头像
          // 等待文件加载完毕再展示
          filereader.onload = function(){
              $('#img').attr('src',filereader.result)
          }
      });
  ```

* 后端forms组件

  ```python
  from django import forms
  from django.forms import widgets
  from app01 import models
  
  
  class RegForm(forms.Form):
      username = forms.CharField(max_length=8, min_length=3, label='用户名', error_messages={
          'max_length': '用户名最长不能超过8位',
          'min_length': '用户名最短不能低于3位',
          'required': '用户名必填',
      }, widget=widgets.TextInput(attrs={'class': 'form-control'}))
      password = forms.CharField(max_length=8, min_length=3, label='密码', error_messages={
          'max_length': '密码最长不能超过8位',
          'min_length': '密码最短不能低于3位',
          'required': '密码必填',
      }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
      confirm_password = forms.CharField(max_length=8, min_length=3, label='确认密码', error_messages={
          'max_length': '确认密码最长不能超过8位',
          'min_length': '确认密码最短不能低于3位',
          'required': '确认密码必填',
      }, widget=widgets.PasswordInput(attrs={'class': 'form-control'}))
      email = forms.EmailField(label='邮箱', error_messages={'invalid': '请填写正确的邮箱格式', 'required': '邮箱字段必填'},
                               widget=widgets.EmailInput(attrs={'class': 'form-control'})
                               )
  
      def clean_username(self):
          username = self.cleaned_data.get('username')
          user = models.UserInfo.objects.filter(username=username).first()
          if user:
              self.add_error('username', '用户名已存在')
          return username
  
      def clean(self):
          password = self.cleaned_data.get('password')
          confirm_password = self.cleaned_data.get('confirm_password')
          if not password == confirm_password:
              self.add_error('confirm_password', '两次密码不一致')
          else:
              return self.cleaned_data
  ```

* 后端注册功能

  ```python
  def register(request):
      response_dic = {'code': 100, 'msg': None}
      form_obj = my_form.RegForm()
      if request.method == 'POST':
          form_obj = my_form.RegForm(request.POST)
          if form_obj.is_valid():
              clean_data = form_obj.cleaned_data
              # 删除confirm_password键值对
              clean_data.pop('confirm_password')
              myfile = request.FILES.get('myfile')
              if myfile:
                  clean_data['avatar'] = myfile
              models.UserInfo.objects.create_user(**clean_data)
              response_dic['msg'] = '注册成功'
              response_dic['url'] = '/login/'
          else:
              response_dic['code'] = 101
              response_dic['msg'] = form_obj.errors
          return JsonResponse(response_dic)
      return render(request, 'register.html', locals())
  ```

* 前端ajax提交数据及DOM操作

  ```js
  $('#id_submit').click(function () {
          var formdata = new FormData;
          // 添加普通k,v键值数据
          $.each($('#myform').serializeArray(),function (index,obj) {
              formdata.append(obj.name,obj.value)
          });
          // 添加文件类型数据
          formdata.append('myfile',$('#myfile')[0].files[0]);
          $.ajax({
              url:'',
              type:'post',
              data:formdata,
              // 文件上传需要指定的两个参数
              processData:false,
              contentType:false,
              success:function (data) {
                  if (data.code==100){
                      location.href = data.url;
                  }else{
                      // 先把错误信息清空
                      $('span.error').text('');
                      $('.form-group').removeClass('has-error');
                      $.each(data.msg,function (index,obj) {
                          var target = '#id_' + index;
                          $(target).next().html(obj[0]).parent().addClass('has-error')
                      })
                  }
              }
          })
      });
      // 附加功能 鼠标获取光标移除error样式
      $('input').focus(function () {
          $(this).parent().removeClass('has-error');
          $(this).next().html('')
      })
  ```

### 2.登陆页面

* 页面渲染(拷贝注册页面修改)

  ```html
  <div class="container-fluid">
      <div class="row">
          <div class="col-md-6 col-md-offset-3">
              <h2 class="text-center">登陆</h2>
              <hr>
              {% csrf_token %}
              <div class="form-group">
                  <label for="id_username">用户名</label>
                  <input type="text" id="id_username" name="username" class="form-control">
              </div>
              <div class="form-group">
                  <label for="id_password">密码</label>
                  <input type="text" id="id_password" name="password" class="form-control">
              </div>
              <div class="form-group">
                  <label for="id_code">验证码</label>
                  <div class="row">
                      <div class="col-md-6">
                          <input type="text" id="id_code" name="code" class="form-control">
                      </div>
                      <div class="col-md-6">
                          <img src="/get_code/" alt="" width="380" height="35" id="img_code">
                      </div>
                  </div>
              </div>
              <input type="button" value="提交" class="btn btn-success" id="id_button"><span class="errors"></span>
          </div>
      </div>
  </div>
  ```

* 图片验证码

  ```python
  from PIL import Image, ImageDraw, ImageFont
  from io import BytesIO
  import random
  
  def get_random():
      return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    
  def get_code(request):
      # 推导步骤1：打开图片二进制直接传给前端即可渲染成图片
      # with open('static/img/default.png','rb')as f:
      #     data = f.read()
      # return HttpResponse(data)
  
      # 推导步骤2：图片自动生成
      # img = Image.new('RGB',(380,35),'red')  # 第三个参数支持RGB配色
      # with open('demo.png','wb') as f:
      #     # 调用img里面的save方法保存图片
      #     img.save(f,'png')
      # with open('demo.png','rb')as f:
      #     data = f.read()
      # return HttpResponse(data)
  
      # 推导步骤3：图片保存到内存管理器中
      # io_obj = BytesIO()
      # img = Image.new('RGB',(380,35),'blue')
      # img.save(io_obj,'png')
      # return HttpResponse(io_obj.getvalue())
  
      # 推导步骤4：图片颜色动态生成，图片上动态生成验证码信息
      io_obj = BytesIO()
      img = Image.new('RGB', (380, 35), get_random())
      img_draw = ImageDraw.Draw(img)
      img_font = ImageFont.truetype('static/font/ott.ttf', 25)
  
      code = ''
      for i in range(5):
          random_int = str(random.randint(0, 9))
          random_upper = chr(random.randint(65, 90))
          random_lower = chr(random.randint(97, 122))
          tem_code = random.choice([random_int, random_upper, random_lower])
          img_draw.text((50 + i * 45, 5), tem_code, get_random(), font=img_font)
          code += tem_code
      print(code)
      # 生成的验证码需要保存到session中做后续验证码校验
      request.session['code'] = code
      img.save(io_obj, 'png')
      return HttpResponse(io_obj.getvalue())
  ```

* 后端登陆代码

  ```python
  def login(request):
      response_dic = {'code':100,'msg':''}
      if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          code = request.POST.get('code')
          if request.session.get('code').upper() == code.upper():
              user = auth.authenticate(username=username,password=password)
              if user:
                  auth.login(request,user)
                  response_dic['url'] = '/home/'
              else:
                  response_dic['code'] = 101
                  response_dic['msg'] = '用户名或密码错误'
          else:
              response_dic['code'] = 102
              response_dic['msg'] = '验证码错误'
          return JsonResponse(response_dic)
      return render(request, 'login.html')
  ```

* 前端js代码

  ```js
  <script>
      $('#id_button').click(function () {
          $.ajax({
              url: '',
              type: 'post',
              data: {
                  'username': $("[name=username]").val(),
                  'password': $("[name=password]").val(),
                  'code': $("[name=code]").val(),
                  'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
              },
              success:function (data) {
                  if(data.code==100){
                      location.href = data.url
                  }else {
                      $('.errors').text(data.msg)
                  }
              }
          })
      });
      $('#img_code').click(function () {
          var $oldPath = $(this).attr('src');
          $(this).attr('src', $oldPath += '?')
      })
  </script>
  ```

* 首页搭建(导航条右侧用户展示，登陆注册注销，页面正文布局2,8,2)

  7* admin后台管理表数据录入(phone字段需要再设置blank=True)

  ```python
  """
  添加文章 介绍verbose_name	文章内容先为空
  添加站点
  文章分类:jason分类1，jason分类2，jason分类3
  """
  ```

* 首页所有文章展示

  ```python
  {% for article in article_list %}
              <h4 class="media-heading"><a href="">{{ article.title }}</a></h4>
              <ul class="media-list">
                  <li class="media">
                      <div class="media-left">
                          <a href="#">
                              <img class="media-object" src="/media/{{ article.blog.userinfo.avatar }}" alt="..." width="80">
                          </a>
                      </div>
                      <div class="media-body">
                          {{ article.desc }}
                      </div>
                  </li>
              </ul>
              <span><a href="">{{ article.blog.userinfo.username }}</a></span>
              <span>发布于{{ article.create_time|date:'Y-m-d'}}</span>
              <span><span class="glyphicon glyphicon-comment"></span>评论({{ article.comment_num }})</span>
              <span><span class="glyphicon glyphicon-thumbs-up"></span>点赞({{ article.up_num }})</span>
              <hr>
          {% endfor %}
  ```

* media配置及用户头像显示

  ```python
  # 用户上传的文件存media文件下，模型层定义的文件字段upload_to地址会自动在media下创建
  # 网站用到的静态文件存static文件下
  # 在settings中配置：MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
  # 注意:这里的'media'跟static名字一样，并不是指文件夹名
  
  
  # 如何访问到media文件下所有的资源,static配置了django自动帮我们开启访问接口
  # media文件下所有资源，配置了django也不会自动开启，那如何能让外界能够访问服务器内部资源?手动去开路由
  # from django.views.static import serve
  # from BBStest import settings
  # rl(r'^media/(?P<path>.*)', serve,{'document_root':settings.MEDIA_ROOT})
  
  # 利用上面这种给外界开设访问服务端资源接口方法，可以给任意后端文件开放接口
  # MEDIA_ROOT = os.path.join(BASE_DIR,'app01')  将app01下所有的文件都对外开放接口了
  # url(r'^app01/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),  对外开放服务端内部接口，一定要谨慎
  ```

* 个人站点页面设计(路由设计必须放在最下方)

  ```python
  # 个人站点页面布局3-9
  
  # 路由:url(r'^(?P<username>\w+)/$',views.site)
  
  # 通过名字查询此人是否存在，存在返回个人站点页面，不存在返回404自定义页面
  
  # 404页面直接拷贝博客园404网页源码
  
  # 个人站点css样式文件简单使用
  ```

* 图片防盗链～根据refer信息

## 个人详情

* 侧边栏(文章分类，文章标签，随笔归档)

  ```python
  """
  分组查询中group by谁就以谁做基表
  values在前表示group by,在后表示取值
  filter在前表示where，在后表示having
  
  
  
  """
  # 文章分类，个人博客每个文章分类的文章数
      category_num_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name','c')
  
  # 标签分类 1.先去创建标签与文章的多对多表数据
      tag_num_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name','c')
  
  # 按日期归档
  """
  id		时间					文章内容	  如何以年月分组需要将年月截取出来单独再作为一个字段
  1	  2018-04-24		  111						2018-4
  2	  2019-06-24		  111						2019-6
  3		2019-05-24		  111           2019-5
  4		2019-05-24		  111           2019-5
  5		2019-01-24		  111           2019-1
  
  from django.db.models.functions import TruncMonth
  
  -官方提供
  			from django.db.models.functions import TruncMonth
  			Sales.objects
  			.annotate(month=TruncMonth('timestamp'))  # Truncate to month and add to select list
  			.values('month')  # Group By month
  			.annotate(c=Count('id'))  # Select the count of the grouping
  			.values('month', 'c')  # (might be redundant, haven't tested) select month and count
  			
  时区问题报错
  TIME_ZONE = 'Asia/Shanghai'
  USE_TZ = True
  """
      date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values('month').annotate(c=Count('pk')).values_list('month','c')
  
  # 前端渲染
  {{ month.0|date:'Y年m月'}}
  ```

* 左侧站点的路由设计(参考博客路由模仿设计)

  ```python
   # url(r'^(?P<username>\w+)/category/(?P<id>\d+)',views.site),
   # url(r'^(?P<username>\w+)/tag/(?P<id>\d+)',views.site),
   # url(r'^(?P<username>\w+)/archive/(?P<id>\w+)',views.site),
   # 文章详情路由
  url(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/',views.site),
  ```

* 后端site视图函数

  ```python
    def site(request, username,*args,**kwargs):
      user = models.UserInfo.objects.filter(username=username).first()
      if not user:
          return render(request, 'errors.html')
      # 获取用户个人站点
      blog = user.blog
      # 获取该站点所有的文章
      article_list = blog.article_set.all()
      if kwargs:
          condition = kwargs.get('condition')
          param = kwargs.get('param')
          if condition == 'category':
              # 过滤出当前站点下分类id为1的所有文章
              article_list = article_list.filter(category_id=param)
          elif condition == 'tag':
              # 过滤出当前站点下标签为id为1的所有文章
              tag = models.Tag.objects.filter(pk=param).first()
              # article_list = article_list.filter(tags=tag)
              article_list = article_list.filter(tags__id=param)
          else:
              # 按日期归档
              year,month = param.split('-')
              article_list = article_list.filter(create_time__year=year,create_time__month=month)
  
      # 查询当前站点下每个分类的文章数
      # res = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values('name','c')
      category_num_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c','pk')
  
      # 查询当前站点下每个标签的文章数
      tag_num_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c','pk')
  
      # 查询当前站点下每个月份的文章数
      date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values('month').annotate(c=Count('pk')).values_list('month','c')
      """
      -官方提供
      from django.db.models.functions import TruncMonth
      Sales.objects
      .annotate(month=TruncMonth('timestamp'))  # Truncate to month and add to select list
      .values('month')  # Group By month
      .annotate(c=Count('id'))  # Select the count of the grouping
      .values('month', 'c')  # (might be redundant, haven't tested) select month and count
      """
  
      return render(request, 'site.html', locals())
  ```

* 文章详情界面

  ```python
  """
  1.先做一个模版继承
  2.再将右侧边栏目做成inclusion_tag形式
  3.个人详情页面
  """
  # inclusion_tag
  from django.template import Library
  from app01 import models
  from django.db.models import Count
  from django.db.models.functions import TruncMonth
  
  register = Library()
  
  
  @register.inclusion_tag('left_menu.html')
  def left_menu(username):
      user = models.UserInfo.objects.filter(username=username).first()
      blog = user.blog
      # 查询当前站点下每个分类的文章数
      # res = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values('name','c')
      category_num_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c',
                                                                                                             'pk')
  
      # 查询当前站点下每个标签的文章数
      tag_num_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values_list('name', 'c', 'pk')
  
      # 查询当前站点下每个月份的文章数
      date_list = models.Article.objects.filter(blog=blog).annotate(month=TruncMonth('create_time')).values(
          'month').annotate(c=Count('pk')).values_list('month', 'c')
      """
      -官方提供
      from django.db.models.functions import TruncMonth
      Sales.objects
      .annotate(month=TruncMonth('timestamp'))  # Truncate to month and add to select list
      .values('month')  # Group By month
      .annotate(c=Count('id'))  # Select the count of the grouping
      .values('month', 'c')  # (might be redundant, haven't tested) select month and count
      """
      return {'category_num_list':category_num_list,'tag_num_list':tag_num_list,'date_list':date_list,'user':user}
  
    
  # 文章详情
  def article_detail(request, username, article_id):
      article = models.Article.objects.filter(pk=article_id).first()
      return render(request,'article_detail.html',locals())
  ```

* 文章点赞点踩样式(后端新建专门的视图函数处理点赞点踩请求)

  ```python
  # 拷贝博客样式
  
  # 绑定点击事件，通过hasclass判断true或false间接判断点赞还是点踩
  # 判断当前点击的控件有没有diggit类,如果有是true
    var is_up = $(this).hasClass('diggit')
    
  # 发送ajax请求
  //传的参数是谁(当前登录用户,不需要传,后台直接可以取到)对那篇文章点赞或点踩
                  data: {'article_id':{{article.pk}}, 'is_up': is_up, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
      
  # 后端先校验用户是否登陆
  
  # 获取当前文章id，点赞或者点踩标示，是字符串形式 用json转成python布尔类型
  
  # 再判断当前登陆用户是否已经点赞或点踩过了
  ret = models.UpAndDown.objects.filter(user=request.user, article_id=article_id).first()
  
  # 存数据库
  # 1.先存文章表里的字段信息
  # 2.再存点赞点踩表的信息
                  if is_up:
                      # 点赞,在article表的点赞字段+1
                      models.Article.objects.filter(pk=article_id).update(up_num=F('up_num') + 1)
                      response_dic['msg'] = '点赞成功'
                  else:
                      models.Article.objects.filter(pk=article_id).update(down_num=F('down_num') + 1)
                      response_dic['msg'] = '点踩成功'
                  ret = models.UpAndDown.objects.create(user=request.user, article_id=article_id, is_up=is_up)
                  
  
  # 前端获取当前被点击标签下的span标签，对应文本值加一
  var span = $(this).children('span')
  span.text(Number(span.text()) + 1)  # 注意数据类型
  
  ```

* ```js
  $(".action").click(function () {
              //判断当前点击的控件有没有diggit类,如果有是true
              var is_up = $(this).hasClass('diggit')
              //alert(is_up)
              //取出当前点击div下的span标签
              var span = $(this).children('span')
              console.log(span)
              $.ajax({
                  url: '/diggit/',
                  type: 'post',
                  //传的参数是谁(当前登录用户,不需要传,后台直接可以取到)对那篇文章点赞或点踩
                  data: {'article_id':{{article.pk}}, 'is_up': is_up, 'csrfmiddlewaretoken': '{{ csrf_token }}'},
                  success: function (data) {
                      console.log(data)
                      $("#digg_tips").html(data.msg)
                      if (data.status == 100) {
                          //成功,点赞,或者点踩+1
                          //取到的值,是字符串类型,需要转成int类型
                          //var num=Number(span.text())
                          //span.text(num+1)
                          span.text(Number(span.text()) + 1)
                      }
  
                  }
              })
  
          })
  ```

  ```python
  def diggit(request):
    	"""
    	1.判断用户是否登陆
    	2.判断用户是否已经点过
    	3.判断用户是否点击的自己的文章
    	4.操作数据库记录数据	需要记两条
    	"""
      if request.is_ajax():
          response_dic = {'status': 100, 'msg': None}
          # 必须登录之后才能进行后续操作
          if request.user.is_authenticated():
              article_id = request.POST.get('article_id')
              # 注意传过来的是字符串类型,需要转成布尔类型
              is_up = request.POST.get('is_up')
              is_up = json.loads(is_up)
              # print(type(is_up))
              # print(is_up)
              # 检查是否已经点过了
              ret = models.UpAndDown.objects.filter(user=request.user, article_id=article_id).first()
              if not ret:
                  # 存数据库
                  if is_up:
                      # 点赞,在article表的点赞字段+1
                      models.Article.objects.filter(pk=article_id).update(up_num=F('up_num') + 1)
                      response_dic['msg'] = '点赞成功'
                  else:
                      models.Article.objects.filter(pk=article_id).update(down_num=F('down_num') + 1)
                      response_dic['msg'] = '点踩成功'
                  ret = models.UpAndDown.objects.create(user=request.user, article_id=article_id, is_up=is_up)
              else:
                  response_dic['status'] = 102
                  response_dic['msg'] = '您已经点过了'
          else:
              # 不要重定向
              response_dic['status'] = 101
              response_dic['msg'] = '请先登录'
  
          return JsonResponse(response_dic)
  ```

### 根评论

```python
# 评论区域样式前端搭建

<div>
        <p>发表评论</p>
        <p>
            昵称：<input type="text" id="tbCommentAuthor" class="author" disabled="disabled" size="50"
                      value="{{ request.user.username }}">
        </p>
        <p>评论内容</p>
        <p>
            <textarea name="comment" id="comment" cols="60" rows="10"></textarea>
        </p>
        <p>
            <button class="btn btn-default" id="id_button">提交评论</button>
        </p>
</div>

# 绑定事件发送ajax请求

# 后端校验数据1.校验用户是否登陆，2.利用django orm事务操作添加数据
# 先校验用户是否登陆
        if request.user.is_authenticated():
            article_id = request.POST.get('article_id')
            content = request.POST.get("content")
            with transaction.atomic():
                # 存文章表普通字段数据
                models.Article.objects.filter(pk=article_id).update(comment_num=F("comment_num")+1)
                # 存评论表数据
                models.Comment.objects.create(user=request.user,article_id=article_id,comment=content)
            response_dic['msg'] = '评论成功'
        else:
            response_dic['code'] = 101
            response_dic['msg'] = '请先登陆'
            
# 展示文章所有评论内容	1.前端页面搭建	
	# 仿造:#59楼 2019-03-21 16:49 齐天大胖子
  <div>
    <span>#{{ forloop.counter }}楼</span>
    <span>{{ comment.create_time|date:'Y-m-d H:i:s' }}</span>
    <span><a href="">{{ comment.user.username }}</a></span>
    <span class="pull-right"><a href="">回复</a></span>
  </div>
  	{{ comment.comment }}

# 评论成功后动态渲染评论内容ajax渲染与render渲染不一样
			if (data.code == 100) {
              var content = $("#comment").val();
              var username = "{{ request.user.username }}";
              // 一旦成功先清空用户输入的值
              $('#comment').val('');
              str = `
                  <li class="list-group-item">
                  <div>
                  <span>${username}:</span>
                  </div>
                  ${content}
                  </li>
              `;
              $('.list-group').append(str)
                    }

```

### 子评论提交

* 点击回复按钮干两件事，在输入框里面加@+父评论人名并回车，存储父评论id值

* 由于还是点击提交按钮发送ajax请求，所以存储父评论id值的变量应该定义在全局并且提交评论内容的时候，需要判断当前评论是否是子评论，如果是需要将@+父用户名切除掉

  ```html
  
  <script>
    // 需要定义一个全局变量存储父评论id值
          var parentId = '';
    // 评论相关代码
          $('#id_button').click(function () {
              // 获取textarea内容
              var content = $('#comment').val();
              // 如果parentId有值
              // 需要收到将@用户名切除掉
              if (parentId){
                  var index = content.indexOf('\n') + 1;
                  content = content.slice(index)
              }
              $.ajax({
                  url: '/comment/',
                  type: 'post',
                  data: {
                      'article_id': "{{ article.pk }}",
                      'content': content,
                      // 父评论id，由于数据库设置为改字段可为空，所以传空也没有关系
                      'parent_id':parentId,
                      'csrfmiddlewaretoken': "{{ csrf_token }}"
                  },
  $(".reply").click(function () {
              parentId = $(this).attr('comment_id');
              var name = $(this).attr('username');
              // 写上@用户名
              $("#comment").val('@'+name+'\n');
              // 获取光标
              $('#comment').focus();
  
          })
  </script>
  
  ```

* 子评论render显示(在回复消息上面加@+回复的人名)在循环渲染评论内容的时候加if判断即可

  ```python
  {% if comment.parent %}
  <p>@{{ comment.parent.user.username }}</p>
  {% endif %}
  {{ comment.content }}
  ```

* 小bug调试(每次提交请求时判断是否时子评论，如果是要把全局的parent_id清空)

  ```html
  <script>
  $('#id_button').click(function () {
              // 获取textarea内容
              var content = $('#comment').val();
              // 如果parentId有值
              // 需要收到将@用户名切除掉
              if (parentId) {
                  var index = content.indexOf('\n') + 1;
                  content = content.slice(index)
              }
              $.ajax({
                  url: '/comment/',
                  type: 'post',
                  data: {
                      'article_id': "{{ article.pk }}",
                      'content': content,
                      // 父评论id，由于数据库设置为改字段可为空，所以传空也没有关系
                      'parent_id': parentId,
                      'csrfmiddlewaretoken': "{{ csrf_token }}"
                  },
                  success: function (data) {
                      if (data.code == 100) {
                          var content = $("#comment").val();
                          var username = "{{ request.user.username }}";
                          // 一旦成功先清空用户输入的值
                          $('#comment').val('');
                          if(parentId){
                              // 清空parentId 不然后面所有提交的根评论都变成子评论
                              parentId = '';
                          }
                          str = `
                  <li class="list-group-item">
                      <div>
                          <span>${username}:</span>
                      </div>
                      ${content}
                  </li>
                          `;
                          $('.list-group').append(str)
  
                      }
                  }
              })
          });
  </script>	
  ```

* 后台管理

  ```python
  # 模版文件夹中建一个后台管理文件夹backend，在里面写后台管理相关的模版文件
  
  # 利用bootstrap js插件搭建后台管理页面
  
  # 模版继承，添加文章页面搭建，利用kindeditor开源编辑器
  
  # 文章提交直接利用form表单提交的方式完成文章的添加
  
  # 功能完善
  """
  1.文本的截取应该只截文字
  2.防止xss攻击:写在文章里和直接写在原生html标签里是不一样的
  
  可以直接用正则，也可以用bs4快速完成
  """
  @login_required(login_url='/login/')
  def add_article(request):
      if request.method == 'GET':
          return render(request, 'backends/addarticle.html')
      else:
          title = request.POST.get('title')
          content = request.POST.get('content')
          # 处理xss攻击和取出150个文本字符
          # 第一个参数：要解析的html的内容，第二个参数，是解析的方式
          soup = BeautifulSoup(content, 'html.parser')
          # print(soup.text)提取所有的文字内容
          tags = soup.find_all()  # tags 是所有的标签
          for tag in tags:
              # tag.name取到标签的名字
              # print(tag.name)
              if tag.name == 'script':  # # 取出script标签，删除
                  tag.decompose()
          # 截取150个字符
          desc = soup.text[0:150]
          ret = models.Article.objects.create(title=title, desc=desc, content=str(soup), blog=request.user.blog)
          return redirect('/backend/')
  ```

* 上传图片

  ```python
  # 富文本编辑器上传图片需要手动配置图片上传的路径,后端再开一个接收富文本编辑上传图片的接口,由于上传图片也是post请求，所以需要解决csrf校验的问题
  # kindeditor文档初始化参数配置中搜索extra配置
  KindEditor.ready(function (K) {
              window.editor = K.create('#editor_id', {
                  width: '100%',  # 调宽度
                  height:'650px',  # 调高度
                  resizeType:0,  # 调textarea是否支持缩放
                  uploadJson : '/upload_img/',  # 图片上传的请求路径
                  extraFileUploadParams:{  # post请求携带额外参数
                      'csrfmiddlewaretoken':'{{ csrf_token }}'
                  }
              });
          });
  
  # 文件上传到后端，路径配置，存放于media文件夹下，再创建一个专门存档富文本编辑器图片的文件夹如article_img
  
  
  import os
  from BBStest import settings
  def upload_img(request):
      print(request.FILES)
      response_dic = {'error':'','message':''}
      file_obj = request.FILES.get('imgFile')
      if file_obj:
          # 文件路径
          path = os.path.join(settings.BASE_DIR,'media','article_img')
          # 判断改文件夹是否存在，不存在自动创建
          if not os.path.exists(path):
              os.mkdir(path)
          img_path = os.path.join(path,file_obj.name)
          # 文件操作存储图片文件
          with open(img_path,'wb') as f:
              for line in file_obj:
                  f.write(line)
          """
          针对富文本编辑器上传图片需要使用别人规定的写法格式
                 //成功时
              {
                      "error" : 0,
                      "url" : "/path/to/file.ext"
              }
              //失败时
              {
                      "error" : 1,
                      "message" : "错误信息"
          """
          response_dic['error'] = 0
          response_dic['url'] = '/media/article_img/%s'%file_obj.name
      else:
          response_dic['error'] = 1
          response_dic['message'] = '上传图片错误'
      return JsonResponse(response_dic)
  ```

## BBS项目总结

```reStructuredText
-BBS总结：
		1 登陆功能：
			-图形验证码
			-ajax提交
			-认证用的是auth
			-认证通过，login
		2 注册功能
			-forms组件
			-ajax提交
			-错误信息渲染
		3 首页
			-全部文章取出来（分页）for循环渲染
		4 个人站点
			-文章展示（当前站点的所有文章）
			-左侧标签显示
				-三个分组查询，TruncMonth
			-抽取成inclusion_tag
			-左侧过滤
		5 文章详情
			-继承了母版
			-marksafe展示html
		6 点赞点踩
			-事务
		7 评论
			-根评论
				-根评论提交
				-根评论render显示
				-根评论ajax显示
			-子评论
				-子评论提交
				-子评论render显示
				-子评论ajax显示
		8 后台文章展示
			-table的展示
		9 新增文章
			-富文本编辑器使用
			-富文本编辑器上传图片
			-处理xss攻击（bs4）
```



