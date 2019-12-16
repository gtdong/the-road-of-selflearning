### django请求生命周期
```python
路由层:路由与视图函数对应关系，但是视图函数可以是真正的函数也可以是类 
    FBV：基于函数的视图
    CBV：基于类的视图
        判断当前请求方式在不在默认的八个请求方式内
	然后根据反射回去到字符串方法名所对应的对象中的方法
	调用该方法返回相应结果
class MyLogin(View):
	def get(self,request):
		pass
	def post(self,request):
		pass

obj = MyLogin()
handler = getattr(obj,request.method.lower())
return handler()
```

```python
- 正则表达式
	url(正则表达式,视图函数内存地址)
- 无名分组
	url(r'^edit/(\d+)/',views.edit_view)  #会将\d+ 匹配到的数字当做位置参数传递给后面的视图函数
- 有名分组
	url(r'^edit/(?P<edit_id>\d+)/',views.edit_view)  #会将\d+ 匹配到的数字当做关键字参数传递给后面的视图函数
- 反向解析
	url(r'^edit/(?P<edit_id>\d+)/',views.edit_view，name='app01_add')
	起别名千万不要重复
	当有多个app存在的情况下，起别名的时候推荐你加上应用前缀
		app01
		app02
		app03
		
	前端  
		{% url 别名%}
		
		有名无名
		{% url 别名 args1 args2 %}
	后端
		reverse('别名')
		无名分组
		reverse('别名',args=(1,))
		有名分组
		reverse('别名',args=(1,))
- 路由分发
	当一个django项目下面有多个app的情况下，总的urls.py中路由与视图函数的对应关系太多 不便于管理
	这个时候就可以再每个app下创建自己的urls.py，总的urls.py不再做对应关系，而只是做分发任务
	
	
	每个app下都可以有自己的urls.py  static文件夹   templates模板文件
	也就意味着 每个app都可以被独立的开发出来  而不需要讨论交互(******)
```	
	
	



### 伪静态
```python
	url名带有.html后缀，看起来像是静态文件
虚拟环境
	每个项目都可以有专门属于自己项目的开发环境
Django2.0
	django2.0中
		path  第一个参数不支持正则 写什么就匹配什么
		re_path 就等价于django1.0中的url
jsonresponse
	返回json格式的数据
	json.dumps({'name':'矮跟'},ensure_ascii = False)
	JsonResponse(dic,json_dumps_params={'ensure_ascii':False})

fbv与cbv
	



模版语法传值
	变量相关 {{}}
	逻辑相关 {%%}
	
	传值的时候 如果是函数或者是方法  会自动加括号调用 将函数或者方法的返回结果展示到前端
	模板语法不支持给函数传参
```
	
	

### 过滤器及标签
```python
	{{ 1|add:1}}
	|date:"Y-m-d"
	213210312|filesizeformat
	|truncatechars
	|truncatewords
	
	
	
	{% if %}
	
	{% elif %}

	{% endif %}

	{%for item in l%}
		{{forloop}}
		first
		last
		counter0
		counter
	{%empty%}
		
	{%endfor%}
```python
	
### 模版的继承与导入
```
	{% extends  '模板名'%}
	
	{% block content %}
	{% endblock %}
	
	
	{% include  '子板名'%}
```

```python
单表操作
	

常用查询方法

图书管理系统表设计

外健字段的增删改查

跨表查询

	正向查询按字段
	反向查询按表名小写
		如果是一对一的话 不需要加_set
		其余两种情况都需要加_set
			app01.Book.None  如果看到该结果  说明你的orm语句最后少了一个.all() 仅此而已
			
			
	外键字段的建立符合以下规律
		一对一和多对多 外键字段建在任意一张表都可以  但是推荐你建在查询频率较高的那张表
		一对多 建在多的那一方
		
			
	基于对象的跨表查询(子查询)
		
	
	
	基于双下滑线的跨表查询(连表查询)
	
	
	
	
聚合与分组查询
查看sql语句的第一种方式
		LOGGING = {
			'version': 1,
			'disable_existing_loggers': False,
			'handlers': {
				'console':{
					'level':'DEBUG',
					'class':'logging.StreamHandler',
				},
			},
			'loggers': {
				'django.db.backends': {
					'handlers': ['console'],
					'propagate': True,
					'level':'DEBUG',
				},
			}
		}
必须是queryset对象才可以调用的方法  
	queryset.query也能够查看到当前queryset对象所对应的sql语句
		
		
	聚合查询  
		聚合函数  分组之后可以使用聚合函数
			max
			min
			avg
			sum
			count
		from django.db.models import Max,Min,Avg,Sum,Count
		
		
	分组查询  annotate
	
F与Q查询


事务(ACID)
	A：原子性
	C：一致性
	I：隔离性
	D：持久性
	from django.db import transaction
    try:
        with transaction.atomic():
            # 订单表 创建记录
            models.Order.objects.create(number=...,date=...,addr=...)
            # 书籍表 库存减一 卖出加一
            models.Book.objects.filter(id=1).update(kucun = F('kucun') -1,maichu=F('maichu') + 1)
    except BaseException as e:
        print(e)


	MTV与MVC
	MVC：
		M：models
		V:views
		C:controller
	
	MTV:
		M:models
		T:templates
		V:views
	ps:MTV本质也是MVC
	
	

	多对多表关系的三种创建方式
	1.全自动
		authors = models.ManyToManyField(to='Author')
		让django orm自动帮你创建第三张表
		好处:不需要自己手动添加
		坏处:表字段的扩展性极差   只会帮你建外键字段  其他额外字段一概无法创建
	2.纯手动(了解)
		class Book(models.Model):
			name = ...
		class Author(models.Model):
			name = ...
			
		class Book2Author(models.Model):
			book_id = models.ForeignKey(to='Book')
			author_id = models.ForeignKey(to='Author')
	3.半自动
		class Book(models.Model):
			name = ...
			authors = models.ManyToManyField(to='Author',through='Book2Author',through_fields=('book','author'))
		class Author(models.Model):
			name = ...
			books = models.ManyToManyField(to='Author',through='Book2Author',through_fields=('author','book'))
		class Book2Author(models.Model):
			book = models.ForeignKey(to='Book')
			author = models.ForeignKey(to='Author')
			create_time = ...
			info = ...
```
### 多对多关系建立

### ajax简介
```
局部刷新
异步提交
	
	
	
	我们所学的ajax是基于jQuery的  你在书写一定要确保到了jQuery文件
	
	小实例
		在页面上生成三个input框
		前两个用户输入数字完毕之后点击提交按钮 自动算出和
```
### ajax使用
```python
	JSON.stringify({'name':'jason','password':'123'})  # 等价于 json.dumps()
	JSON.parse()										# 等价于json.loads()
	
	ContentType:表示数据的编码格式
	前后端传输数据的编码格式
		urlencoded
			是form表单和ajax都默认的编码格式
			urlencoded数据格式
				i1=1&i2=2
			django后端会将符合urlencode编码格式的数据 解析并放入request.POST中
			
		formdata
		
		application/json
	
	
	
	基本使用
	发送的数据的时候 你不能骗人家
	数据格式和编码要一致 不能数据时urlencoded格式 编码却指定成了json格式
	
	
	1.发送普通数据
		$.ajax({
            url:'',  // 控制数据的提交目的地  不写默认就是当前页面所在的url
            type:'post',  // 控制提交方式
            data:{'i1':$('#i1').val(),'i2':$('#i2').val()},  // 提交的数据
            success:function (data) {  // 形参data接收的到就是异步提交返回的结果   形参data和上面的data无关 
                $('#i3').val(data)
            }
        })
	2.发送json格式数据
		django针对json格式的数据  不做任何处理
		
	3.ajax发送文件
		需要借助于内置对象FormData
```
		
### 自定义分页器使用





### forms组件
```python
	注册页面
		获取用户输入
		判断用户输入是否合法
		如果不合法展示错误信息
		
	
	
	forms组件能够干的事
		1.前端页面搭建
		2.后端数据校验
		3.展示错误信息
	1.后端数据校验
		forms组件中字段默认都是必须传值的
		forms组件默认不能少传字段 但是可以多传字段  多传的字段form组件直接忽略不考虑
		
		
		class MyRegForm(forms.Form):
			name = forms.CharField(max_length=8)  # name字段最大只能是八位
			password = forms.CharField(max_length=8,min_length=3)  # 最大八位 最少三位
			email = forms.EmailField()  # email字段接收的数据  必须符合邮箱格式
		forms组件的使用  第一步生成一个继承form类的类
		from app01 import views
		obj = views.MyRegForm({"name":'jason','password':'12','email':'123'})
		# 判断信息是否完全合法
		obj.is_valid()
		# 获取字段及错误信息
		obj.errors
		{'password': ['Ensure this value has at least 3 characters (it has 2).'],
		 'email': ['Enter a valid email address.']}
		# 获取符合条件的数据
		obj.cleaned_data
			
	2.渲染标签
		forms组件只会帮你渲染input框  form标签和submit提交按钮都需要你自己写
```	
		
	

### cookie，session

```python
	cookie:就是保存在浏览器上的键值对
	session:就是保存在服务器的上的键值对
	
	
	
	
	django用session一定要先初始化django默认的那些表
	django服务端会自动生成一串随机字符串  保存到浏览器上  键固定就叫sessionid
	
	django默认的session过期时间是14天
	
	
	
	request.session['k1'] = 'xxx'
	"""
		1.内部自动生成一个随机字符串
		2.将键值对保存到django_session表中
		3.将生成的随机字符串发送给浏览器保存起来
	"""
	request.session.get('k1')
	"""
		1.内部自动获取浏览器的随机字符串
		2.取django_session表中依次查找
		3.获取对应的信息 赋值给request.session
	
	
	"""
	
	index  home  xxx
	基于session写一个登录验证
	比如说有是个视图函数 必须用户登录之后才能查看
	你写一个装饰器完成该功能
	拔高:用户登录完成后跳转到用户没有登录之前想要访问的那个页面
	
```	
	
	

### django中间件

```python
	django中间件就类似于是django的保安
	消息来的时候和响应走的时候 都必须进过中间件
	
	中间件可以做全局的访问频率校验 身份校验 。。。
	只要是涉及到全局的 你都可以考虑使用中间件来做！！！
	
	django默认有七个中间件，也支持用户自定义中间件
	自定义中间件 django暴露给用户五个可以自定义的方法
	
	MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
	五个方法:
		掌握
		process_request:请求来的时候 会依次(从上往下的顺序如上图)执行每一个中间件里面的process_request方法(如果没有定义那么直接通过)
		process_response:响应走的时候 会依次(从下往上的顺序)执行每一个中间件里面的process_response方法
		了解
		process_views
		process_templates_response
		process_exceptions
	
	
	自定义中间件	
		1.新建一个任意名称的py文件
		2.文件内 写类继承中间件的总类
```
	
	

### csrf跨站请求伪造
	钓鱼网站

### auth模块  

### BBS表设计







