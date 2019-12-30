### 软件开发架构
* b/s:
  * broswer 浏览器
  * server  服务器
* c/s：
  * client  客户端
  * erver  服务端
ps:bs本质也是cs
### HTTP协议
超文本传输协议
	
四大特性：
* 1.基于TCP/IP之上作用于应用层的协议
* 2.基于请求响应
* 3.无状态
    cookie
    session
    token
* 4.无连接
    websocket

### http数据格式
* 请求格式
  * 请求首行 GET /index HTTP/1.1 
  * 请求头(一大堆k,v键值对)
  * 请求体(数据)
		
		
* 响应格式
  * 响应首行 HTTP/1.1 200 OK 
  * 响应头(一大堆k,v键值对)
  * 响应体(数据)
### HTTP响应状态码
10X:服务端已经接受到你的数据了 你可以继续提交数据进行下一步操作  
20X :请求成功(200)  
30X:重定向(301,302)  
40X:请求错误(404)  
50X:服务端错误(500)
		

### GET请求与POST请求   
  * GET请求:获取页面资源
  * POST请求:朝服务端发送数据(让服务端校验该数据)
* views.py
视图函数
*  urls.py
路由与视图函数的映射关系
		
### 动静态网页
* 静态网页
  * 数据是写死的 万年不变
* 动态网页
  * 数据是实时获取的 一直在改变(eg:数据库的数据，当前时间)

		
		
### 模板渲染(雏形)
后端产生数据直接传递给前端页面 前端页面获取数据通过模板语法展示
	
### 模板语法
```html
{{}}(变量名相关)  获取后端传递的数据 通过变量名
{%%}(逻辑相关)

jinja2模板语法 极为接近后端python语法

{{ data }}
<p>{{data.username}}</p>
<p>{{data['password']}}</p>
<p>{{data.hobby.0}}</p>
<p>{{data.hobby.1}}</p>


{%for user_dict in user_list%}
    <tr>
	<td>{{user_dict.id}}</td>
	<td>{{user_dict.username}}</td>
	<td>{{user_dict.password}}</td>
    </tr>
{%endfor%}
```

### python三大主流web框架
a: socket服务  
b: 路由与视图函数映射关系  
c: 模板渲染
* django:大而全 类似于航空母舰
  * a用的别人的 wsgiref  上线之后会换成uwsgi
  * b自己写的
  * c自己写的
		
	
* flask:小而精  类似于游骑兵
  * a用的别人的  werkzeug  
  * b自己写的
  * c用的别人 jinja2
	
* tornado:异步非阻塞
  * 三者都是自己写的
		
		
		
### django
#### 注意事项
  * 1.计算机名称不能含有中文
  * 2.一个pycharm窗口就是一个工程(项目)
  * 3.项目文件夹不要有中文
  
#### ps:django版本问题
  * django 1.X
  * django 2.X
#### 安装
`pip3 install django == 1.11.11`
#### 命令行
```shell
#创建django项目
django-admin startproject 项目名
ps:创建一个应用名的文件夹 里面有一个跟应用名同名的文件夹和一个manage.py文件
#创建应用
django-admin startapp 应用名
#启动django项目
python3 manage.py runserver

#ps:
#1.命令行创建django项目不会自动新建templates文件夹,并且settings配置文件不会自动写templates文件夹路径
#2.在django中创建的应用必须去settings文件中注册才能生效,否则django不识别
#3.确保不要端口冲突	
```
#### application
  * 一个django项目 可以有多个应用
  * django是一款开发应用的web框架
  * django项目就类似是一所大学
  * 而里面的应用就类似于一个个学院
	
	
	
#### 项目名

#### 应用名文件夹
  * migrations文件夹: 数据库迁移记录
  * admin.py: django admin后台管理相关
  * models.py: 模型类
  * views.py: 视图函数
		
#### 项目同名文件夹
  * settings.py: django暴露用户可配置的配置文件
  * urls.py: 路由与视图函数映射关系
  * templates: 所有的html文件
  * manage.py: django入口文件
		
	
			
#### django小白必会三板斧
  * HttpResponse:返回字符串
  * render:返回html页面
  * redirect:重定向


#### 静态文件
网站所用到的已经写好的文件(css,js,图片) 
通常网站所用到的静态文件都会存放到static文件夹
	

#### django静态文件配置
```python
STATIC_URL = '/static/'  # 接口前缀
STATICFILES_DIRS = [
	os.path.join(BASE_DIR,'static'),
]
```	
```html	
{% load static %}
<link rel="stylesheet" href="{% static 'bootstrap-3.3.7/css/bootstrap.min.css'%}">
<script src={% static "bootstrap-3.3.7/js/bootstrap.min.js"%}></script>
```

`
form表单默认是get请求 
get请求携带的参数是拼接在url后面的以?开头&链接   
ps:get请求可以携带参数 但是参数的大小有限制 最大4KB，并且是明文的   
http://127.0.0.1:8000/login/?username=jason&password=123
`
	
获取用户输入的框 都必须要有name属性
	
	
#### action参数有三种写法
  * 1.什么都不写 默认往当前页面的url地址提交
  * 2.只写路由后缀(******)
  * 3.写全路径
		


#### pycharm连接数据库
#### django连接mysql
```python
#1.配置文件中配置
DATABASES = {
'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'day19',
	'USER':'root',
	'PASSWORD':'123',
	'HOST':'127.0.0.1',
	'PORT':3306,
	'CHARSET':'utf8'
}
}
#2.去应用名下的__init__.py或者项目名下的__init__.py文件中 告诉django不要使用默认的mysqld_db模块连接mysql而是使用pymysql
import pymysql
pymysql.install_as_MySQLdb()
```

	
#### ORM(对象关系映射)
  * 类	>>>	数据库的表

  * 对象	>>>	数据库里面的一条条的表记录

  * 对象点属性	>>>	表记录的某个字段对应的值

ps:
* 能够让一个不会数据库操作的人 也能够通过编程语言轻松的操作数据库
* 有时候sql语句的查询效率可能偏低
			

			
#### django orm注意事项
  * 1.django orm不会帮你自动创建库 只能帮你自动创建表
  * 2.models.py中写模型类
  * 3.执行数据库迁移(同步)命令
```
python3 manage.py makemigrations  将数据的更改操作记录到小本本上
python3 manage.py migrate  将更改真正同步到数据库
```
		
		
		
		
#### 编辑
  * 基于已经存在了的数据进行修改
  * 先将用户想要修改的数据查询出来 并且展示给用户看
  * 用户修改完之后发送post请求 后端修改数据			
#### 数据的增删改查
```python
增
1.create()
	modeles.User.objects.create(kwargs)
	create方法会返回当前所创建的数据对象(*****)
2.对象.save()
	user_obj = models.User()
	user_obj.username = 'jason'
	user_obj.save()
	
	
删
queryset对象.delete()


改
1.update()
	models.User.objects.filter(kwargs).update()
	批量更新

2.对象.save()
	user_obj = models.User(kwargs)
	user_obj.username = 'jason'
	user_obj.save()
	效率较低
	
	
查

1.all()  查所有 不需要传参数
2.filter(kwargs)  结构是一个queryset对象 你可以把它看成一个列表里面是一个个的数据对象
```				
django的视图函数返回的是一个HttpResponse对象

#### django请求生命周期		
	
```
request.GET  获取get请求携带的参数
request.POST  获取post请求携带的参数
	上面两者在用get取值的时候 默认取列表最后一个元素
	如果想整体取用getlist
request.method  获取当前请求方式
```





	
	
		
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
