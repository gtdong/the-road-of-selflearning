上周内容回顾
	django
	
	手动实现简易版本的web框架
	
	HTTP协议
		四大特性
			1.基于TCP/IP作用于应用层的协议
			2.基于请求响应的
			3.无状态
			4.无连接
		
		数据格式
			请求/响应
				请求首行
				请求头(一大堆的k，v键值对)
				
				请求体(post请求携带的数据)
				
			响应同上
		
		HTTP协议响应状态码
			1XX:服务端已经接受到了响应的数据 正在处理  你可以继续提交
			2XX:请求成功
			3XX:重定向
			4XX:请求错误(404请求资源不存在)
			5XX:服务端错误(500)
		
	get请求和post请求
		get请求:获取数据
		post请求:提交数据
	
	
	django的安装
		1.计算机的名称最好不要有中文
		2.注意django版本的问题(1.X版本  1.11.11)
		3.一个pycharm窗口只允许一个项目(工程)
		4.路径最好也不要有中文
	
	命令行
		pip3 install django==1.11.11  django如果之前已经装过其他版本不需要手动写在 直接安装 会自动卸载再重装
	测试是否安装成功
		django-admin
	创建django项目
		django-admin startproject mydjangoproject
			在命令所在的位置创建一个名为mydjangoproject文件夹
				mydjangoproject文件夹
					__init__.py
					urls.py  # 总路由  路由(网址 url)与视图函数(处理业务逻辑的函数/类)的对应关系
					wsgi.py
					settings.py  # 项目的配置文件
				manage.py
	创建django应用(application)
		django-admin startapp app01
				app01文件夹
					migrations文件夹  # 数据库改动记录
					__init__.py
					admin.py  # django自带的admin的后台管理
					models.py  # 模型类/表   ORM对象关系映射
					apps.py  # 注册app的时候
					views.py  # 业务逻辑的函数/类代码
					test.py  # 测试文件
		ps：一个django项目可以有多个应用，每个应用都可以有自己的static静态文件夹 templates模板文件夹
			这样的话 就可以实现分任务开发
	
		ps：命令行创建django项目不会自动创建templates文件夹 需要你手动创建并且需要在settings配置文件中指定路径
	
	启动django项目
		python manage.py  runserver
			ps:django默认端口8000
			
	
	
	
	配置文件几个重要的配置
		1.注册app
			每创建一个应用，一定要在settings中注册你的应用 否则django不识别
		2.数据库配置
			1.django默认用的sqlite小型数据库
			可以将其指定成其他的数据库
				 NAME  库的名字
				 HOST
				 PORT
				 USER
				 PASSWORD
			2.数据库配置还需要在__init__.py(项目或者应用的都可以)中告诉django使用pymysql连接mysql
			而不是有默认的mysqldb
			
			
			
		3.静态文件配置
			STATIC_URL = 'static'  # 暴露给用户访问静态文件的接口前缀
			STATICFILES_DIRS = [  # 列表内放的才是真正的静态文件所在的文件夹路径
					os.path.join(BASE_DIR,'static')，
					os.path.join(BASE_DIR,'static1')，
					os.path.join(BASE_DIR,'static2')，
				]
			
			前端动态解析静态文件接口前缀
				{% load static %}
				{% static "bootstrap-3.3.7/js/bootstrap.min.js"%}
	
			
		django小白必会三板斧
			HttpResponse  # 返回字符串
			
			render  # 返回html页面
			
			redirect  # 内部重定向
			
		数据库迁移命令
			ps:django默认没有char字段 只有varchar 但是可以自定义char字段
			
			主要在models.py中动了跟数据库相关的代码，就必须执行数据库迁移的两条命令
				1.python manage.py makemigrations  # 将改动记录记录到小本本上
				2.Python manage.py migrate  # 真正的数据库操作命令
				ps:当上述完整的命令记住之后可以使用简单版本的
				TOOLS>>>run manage.py task
				
				
		
	登录注册
		django获取前端信息
			request.POST  # 获取的post提交的数据
			request.GET  # 获取get请求携带的数据   get请求携带的参数 数据量是由大小限制的 大概在4KB左右
				/index?id=1&password=2
			ps:你可以直接将上述的结果看成是一个大字典
		<QUERYSET {'username':['egon','jason'],'password':[123]}>
		username = request.POST.get('username')  # jason  get获取的永远是列表的最后一个值
		username_list = request.POST.getlist('username')  # ['egon','jason']
		# 上述取值方式 POST GET都一样
		
		
	简单的使用ORM
		create()  # 创建数据
			user_obj = models.User.objects.create(username='jason',password=123)
			user_obj.username
			user_obj.password
			该方法是由一个返回值的 返回值就是当前你所创建的数据对象
		
		filter()  # 查询数据
			该方法返回的结果是一个queryset对象
			你可以把它看成是一个列表，里面放的是一个个的数据对象(juery对象和原生js对象)
		
		update()  # 更新数据
			
		
		delete()  # 删除数据
			
			
			
			

路由层
	路由

视图层
	FBV
	CBV

模板层
	模板语法

模型层
	ORM语法

比较实用的组件
	django中间件
	forms组件
	ajax
	
	auth模块
	
		
			
	ORM
		类         		表
		对象       		表数据
		对象点属性 		表数据所对应的某个字段的值
	
	
	
	
	
	
	django请求生命周期
	
	有名分组和无名分组能否混合使用？
		有名无名不能混合使用！！！
		
		
		
	反向解析
		注意:在起别名的时候 一定要保证 所有的别名都不能重复  必须是唯一的
		
		根据别名动态解析出可以匹配上视图函数之前的url的一个结果
		url(r'^testxxx/',views.test,name='t')
		url(r'^test/(\d+)/$',views.test,name='ttt'),
		前端
			没有正则表达式的反向解析
			{% url 't' %}
			无名分组反向解析
			{% url 'ttt' 1 %}
			有名分组同上
		
		后端
			from django.shortcuts import render,HttpResponse,redirect,reverse
			没有正则表达式的反向解析
			reverse('t')
			无名分组反向解析
			reverse('ttt',args=(1,))
			有名分组同上
			
		
		ps:数字通常是数据库中查出来的数据的主键值
		
	
	
	
	
	
	
			
		
	伪静态
		让一个动态页面伪装成一个看似数据已经写死了的静态页面
		让搜索引擎加大对你这个页面的搜藏力度
		加大seo查询
		
		始终还是抵不过RMB玩家
		
	虚拟环境
		想针对不同的项目 只下载对应用的到的模块
		用不到的一概不要
		
		一个项目分配一个独立的环境
		
		
		
		虚拟环境就类似于你重新又下载了一个python解释器
		
		
	
	django版本区别
		1.X
			路由里面用的是url()
		2.X
			路由里面的用的是path()
		url第一个参数放的是正则表达式
		而你的path第一个参数写什么就是什么，不支持正则
		如果你还想使用第一个参数是正则的方法
		django2.X版本中有一个叫re_path()
		ps:2.x中re_path就等价于1.x中的url
		
		虽然path不支持正则表达式，但是它提供了五种转换器(了解)
	
	JsonResponse
		
	
	
	FBV function based views
	CBV class based views
	
	
	CBV和FBV路由本质是一样的
	都是url+函数内存地址
	
	
	CBV
		url(r'^login/',views.MyLogin.as_view())
		
		from django.views import View
		class MyLogin(View):
			def get(self,request):
				return HttpResponse('get')

			def post(self,request):
				return HttpResponse('post')
	
	
		
		
	模版语法传值
		
		第一种
			return render(request,'demo.html',{'xxx':[1,2,3,4]})
		
		第二种
			return render(request,'demo.html',locals())
		
		前端使用
			{{}}  变量相关
			{%%}  逻辑相关
			
		前后端取消转义
			前端
				|safe
			后端
				from django.utils.safestring import mark_safe


				s2 =  "<h2>我是h2标签</h2>"
				s2 = mark_safe(s2)

	过滤器及标签
	
			标签
			{% if s3.0 %}
				<p>这个东西有值{{ s3 }}</p>
				{% elif s3.1 %}
				<p>有值</p>
				{% else %}
				<p>这个东西是空的</p>
			{% endif %}
			
			
			{% for foo in s %}
				{% if forloop.first %}
				<p>这是我的第一次</p>
					{% elif forloop.last %}
					<p>这是我的最后一次</p>
					{% else %}
					<p>{{ foo }}继续嗨~~~</p>
				{% endif %}
				{% empty %}
				<p>你给我的对象是空的 没办法for循环</p>
			{% endfor %}
			

	模版的继承与导入
		{% extends 'tmp.html' %}  
		在你想做成模板的页面上 添加block块儿 来标识其他用户可以占用的区域
		{% block content %}
                <div class="jumbotron">
                  <h1>Hello, world!</h1>
                  <p>...</p>
                  <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a></p>
                </div>
        {% endblock %}  先在模板中划定区域
		
		
		之后子板利用block就能够找到模板中可以被使用的区域
		
		
		通常情况下 模板中最少有三个区域
			css
			content
			js
		ps:模板中的block块儿越多 页面的可扩展性越高
		
		
		模板到导入
			将一块html页面作为模块的方式 导入使用
			{% include 'goodpage.html' %}
			将goodpage.html页面内容直接导入到该语句的位置
			
单表操作
	DateField()
		auto_now:每次操作该数据的时候 都会自动更新当前时间
		auto_now_add:数据第一次创建的时候 会将创建时间自动记录下来 后续的改动不会再自动更新该字段
	

常用查询方法

图书管理系统表设计
	表关系
		一对一
		一对多
		多对多
		ps:站在两边判断是否可以同时有多个对方
		如果都可以 那么就是多对多
		如果是单向的一对多 那么就是一对多
		如果都不是 要么没有任何关系 要么就是一对一
		
	Book
	
	Publish
	
	Author
	
	AuthorDetail
	
	书和出版社 就是一个一对多
	书和作者   多对多
	作者和作者详情  一对一
	
	
	

	
	
	



外健字段的增删改查

跨表查询

聚合与分组查询

F与Q查询





多对多关系建立

ajax简介

ajax使用

ajax发送文件

自定义分页器使用





forms组件

cookie，session



django中间件

csrf跨站请求伪造

auth模块


		
		
		
		
		
			
			
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
		
		
		
		
		
		
		
		
	
	
	
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
		
		
		
			
			
			
			
			
			
			
			
			
			
			
			
		
	