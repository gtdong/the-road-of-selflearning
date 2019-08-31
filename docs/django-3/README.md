### 外健字段的增删改查

### 跨表查询
```python

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
```
	
	
	
	
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
			



多对多关系建立

ajax简介
	局部刷新
	异步提交
	
	
	
	我们所学的ajax是基于jQuery的  你在书写一定要确保到了jQuery文件
	
	小实例
		在页面上生成三个input框
		前两个用户输入数字完毕之后点击提交按钮 自动算出和
	







ajax使用
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
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
ajax发送文件

自定义分页器使用





forms组件
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
		
		
	

cookie，session
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
	
	
	
	

django中间件
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
		
	
	
	

csrf跨站请求伪造
	钓鱼网站
	
	
	
	




auth模块  




BBS表设计






