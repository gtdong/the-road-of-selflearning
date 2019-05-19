## logging模块

#### 什么是logging模块

logging模块是python提供的用于记录日志的模块

#### 为什么需要logging

我们完全可以自己打开文件然后,日志写进去,但是这些操作重复且没有任何技术含量,所以python帮我们进行了封装,有了logging后我们在记录日志时 只需要简单的调用接口即可,非常方便!

#### 日志级别

在开始记录日志前还需要明确,日志的级别

随着时间的推移,日志记录会非常多,成千上万行,如何快速找到需要的日志记录这就成了问题

解决的方案就是 给日志划分级别

logging模块将日志分为了五个级别,从高到低分别是:

1.info 常规信息

2.debug 调试信息

3.warning 警告信息

4.error 错误信息

5.cretical 严重错误

本质上他们使用数字来表示级别的,从高到低分别是10,20,30,40,50



## logging模块的使用

```python
#1.导入模块
import logging

#2.输出日志
logging.info("info")
logging.debug("debug")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

#输出 WARNING:root:warning
#输出 ERROR:root:error
#输出 CRITICAL:root:critical
```

我们发现info  和 debug都没有输出,这是因为它们的级别不够,

默认情况下:

	logging的最低显示级别为warning,对应的数值为30
	
	日志被打印到了控制台
	
	日志输出格式为:级别  日志生成器名称  日志消息

如何修改这写默认的行为呢?,这就需要我们自己来进行配置

## 自定义配置

```python
import logging
logging.basicConfig()

"""可用参数
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。 
datefmt：指定日期时间格式。 
level：设置rootlogger（后边会讲解具体概念）的日志级别 
"""

#案例:
logging.basicConfig(
    filename="aaa.log",
    filemode="at",
    datefmt="%Y-%m-%d %H:%M:%S %p",
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
    level=10
)
```

#### 格式化全部可用名称

```python
%(name)s：Logger的名字，并非用户名，详细查看
%(levelno)s：数字形式的日志级别
%(levelname)s：文本形式的日志级别
%(pathname)s：调用日志输出函数的模块的完整路径名，可能没有
%(filename)s：调用日志输出函数的模块的文件名
%(module)s：调用日志输出函数的模块名
%(funcName)s：调用日志输出函数的函数名
%(lineno)d：调用日志输出函数的语句所在的代码行
%(created)f：当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d：输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s：字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d：线程ID。可能没有
%(threadName)s：线程名。可能没有
%(process)d：进程ID。可能没有
%(message)s：用户输出的消息
```



至此我们已经可以自己来配置一 写基础信息了,但是当我们想要将同一个日志输出到不同位置时,这些基础配置就无法实现了,

例如 有一个登录注册的功能 需要记录日志,同时生成两份 一份给程序员看,一份给老板看,作为程序员应该查看较为详细的日志,二老板则应该简单一些,因为他不需要关心程序的细节

要实现这样的需要我们需要系统的了解loggin模块

#### logging模块的四个核心角色

1.Logger   日志生成器 产生日志

2.Filter    日志过滤器  过滤日志

3.Handler 日志处理器 对日志进行格式化,并输出到指定位置(控制台或文件)

4.Formater 处理日志的格式



#### 一条日志完整的生命周期

1.由logger 产生日志  -> 2.交给过滤器判断是否被过滤 -> 3.将日志消息分发给绑定的所有处理器 -> 4处理器按照绑定的格式化对象输出日志

其中 第一步 会先检查日志级别 如果低于设置的级别则不执行

第二步 使用场景不多  需要使用面向对象的技术点 后续用到再讲

第三步 也会检查日志级别,如果得到的日志低于自身的日志级别则不输出 

	生成器的级别应低于句柄否则给句柄设置级别是没有意义的,
	
	例如  handler设置为20  生成器设置为30 
	
	30以下的日志压根不会产生

第四步 如果不指定格式则按照默认格式



#### logging各角色的使用(了解)

```python
# 生成器
logger1 = logging.getLogger("日志对象1")

# 文件句柄
handler1 = logging.FileHandler("log1.log",encoding="utf-8")
handler2 = logging.FileHandler("log2.log",encoding="utf-8")

# 控制台句柄
handler3 = logging.StreamHandler()


# 格式化对象
fmt1 = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s:  %(message)s",
    datefmt="%m-%d %H:%M:%S %p")
fmt2 = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s :  %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S")

# 绑定格式化对象与文件句柄
handler1.setFormatter(fmt1)
handler2.setFormatter(fmt2)
handler3.setFormatter(fmt1)

# 绑定生成器与文件句柄
logger1.addHandler(handler1)
logger1.addHandler(handler2)
logger1.addHandler(handler3)

# 设置日志级别
logger1.setLevel(10)    #生成器日志级别
handler1.setLevel(20)   #句柄日志级别

# 测试
logger1.debug("debug msessage")
logger1.info("info msessage")
logger1.warning("warning msessage")
logger1.critical("critical msessage")
```

到此我们已经可以实现上述的需求了,但是这并不是我们最终的实现方式,因为每次都要编写这样的代码是非常痛苦的

#### logging的继承(了解)

可以将一个日志指定为另一个日志的子日志 或子孙日志

当存在继承关系时 子孙级日志收到日志时会将该日志向上传递

指定继承关系:

```python
import  logging

log1 = logging.getLogger("mother")
log2 = logging.getLogger("mother.son")
log3 = logging.getLogger("mother.son.grandson")

# handler
fh = logging.FileHandler(filename="cc.log",encoding="utf-8")
# formatter
fm = logging.Formatter("%(asctime)s - %(name)s -%(filename)s - %(message)s")

# 绑定
log1.addHandler(fh)
log2.addHandler(fh)
log3.addHandler(fh)
# 绑定格式
fh.setFormatter(fm)
# 测试
# log1.error("测试")
# log2.error("测试")
log3.error("测试")
# 取消传递
log3.propagate = False
# 再次测试
log3.error("测试")
```



#### 通过字典配置日志模块(重点)

每次都要编写代码来配置非常麻烦 ,我们可以写一个完整的配置保存起来,以便后续直接使用

```python
import logging.config
logging.config.dictConfig(LOGGING_DIC)
logging.getLogger("aa").debug("测试")
```

**LOGGING_DIC模板**

```python
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'
logfile_path = "配置文件路径"

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5, #日志文件最大个数
            'encoding': 'utf-8',  # 日志文件的编码
        },
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        'aa': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
```

补充:

getLogger参数就是对应字典中loggers的key , 如果没有匹配的key 则返回系统默认的生成器,我们可以在字典中通过空的key来将一个生成器设置为默认的

```python
'loggers': {
    	# 把key设置为空
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
```

,往后在使用时可以这调用模块提供的函数,来输出日志

logging.info("测试信息!")

另外我们在第一次使用日志时并没有指定生成器,但也可以使用,这是因为系统有默认的生成器名称就叫root



最后来完成之前的需求:

有一个登录注册的功能 需要记录日志,同时生成两份 一份给程序员看,一份给老板看,作为程序员应该查看较为详细的日志,二老板则应该简单一些,因为他不需要关心程序的细节

```python
# 程序员看的格式
standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]' #其中name为getlogger指定的名字
logfile_path1 = "coder.log"

# 老板看的格式
simple_format = '[%(levelname)s][%(asctime)s]%(message)s'
logfile_path2 = "boss.log"


LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        #打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        #打印到文件的日志,收集info及以上的日志
        'std': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path1,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5, #日志文件最大个数
            'encoding': 'utf-8',  # 日志文件的编码
        },
        'boss': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': logfile_path2,  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 日志文件最大个数
            'encoding': 'utf-8',  # 日志文件的编码
        }
    },
    'loggers': {
        #logging.getLogger(__name__)拿到的logger配置
        'aa': {
            'handlers': ['std', 'console',"boss"],  # 这里把上面定义的handler都加上，即log数据会同时输出到三个位置
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
```