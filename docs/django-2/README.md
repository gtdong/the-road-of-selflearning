### 今日内容
```python
路由层
	路由

视图层
	FBV
	CBV

模板层
	模板语法

模型层
	ORM语法
```

### 比较实用的组件
* django中间件
* forms组件
* ajax
* auth模块	
### ORM
```python
类         		表
对象       		表数据
对象点属性 		表数据所对应的某个字段的值
```
### django请求生命周期
	
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


		
		
		
		
		
			
			
		
		
		
		
		
		
		
		
		
		
		
		
