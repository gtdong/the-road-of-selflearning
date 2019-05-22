## 复习

```python
'''
装饰器
@wraper  # fn = wraper(fn)
def fn(): pass

def wrap(arg):
	def outer(func):
		# 可以用arg
		def inner(*args, **kwargs):
			# 可以用arg
			res = func(*args, **kwargs)
			return res
		return inner
	return outer

@wrap('实参')
def fn(): pass

# 更改inner的文档注释指向
from functools import wraper

三元表达式：a if a > b else b

列表、字典推导式: [v for v in iterable] {k: v for k, v in iterable}
['奇数' if v % 2 == 1 '偶数' for v in range(1, 11)]

迭代器:
# 有__iter__() => 可迭代对象
# 有__next__() => 迭代器对象
# for迭代器
# enumerate => 为可迭代对象生成索引

生成器：自定义的迭代器
# range
def fn():
	msg = yield 1	
	yield 2
obj = fn()
obj.__next__()
obj.send(msg)

递归:函数的自调用
# 回溯
# 递堆
# 条件与出口

匿名函数：lambda


内置函数：max | min | sorted | map | reduce
max(dic, key=lambda k: dic[k])



'''
```

## 今日内容

```python
'''
1.模块
	-- 模块的概念
	-- 模块的使用
	-- 解决循环导入
	
2.包
	-- 包的概念
	-- 包的管理 ***


3.常用模块
	-- sys | os | time | datetime | json | random
	-- re | logging | hashlib
'''
```





## 模块

```python
# 模块的概念：一系列功能的集合体，可以给其他文件提供功能（数据）

'''
常见的四种模块：
1.使用python编写的.py文件
2.把一系列模块组织到一起的文件夹（注：文件夹下有一个__init__.py文件，该文件夹称之为包）
3.使用C编写并链接到python解释器的内置模块
4.已被编译为共享库或DLL的C或C++扩展
'''


# 模块的创建与使用
# 1.将具有共性的功能放在一个py文件中，这样的文件就可以称之为模块
# 2.将封装好的模块对外提供功能
# 3.在要使用模块功能的地方进行导入 => 使用功能
# 语法：import 模块名



# m1.py
def t1():pass
def t2():pass
def t3():pass


# 导入模块完成了哪些事
import m1  # m1名字就是模块m1的文件对象，存放的是m1文件的地址
# import导入模块完成的事情：
# 1.将被导入的模块编译成模块名对应的pyc文件
# 2.从上至下执行被调用模块的所有代码，形成模块的名称空间，将模块中产生的所有名字存放在模块的名称空间中
#       -- t1,t2,t3存放在m1模块的名称空间中
# 3.在要使用模块的文件(当前文件)的名称空间中产生一个与模块名同名的名字指向模块的名称空间
# print(m1)


# 重点：在一个文件中直接使用名字，一定找当前文件中的名字

# 执行文件与模块的名称空间如果建立起联系的：通过导入的模块名，所以执行文件访问模块文件中的名字用
#		-- 模块名.模块中的名字
```



## 模块别名

```python
import 模块名 as 别名

# 1.模块名与当前文件中的名字发生冲突，用起别名解决冲突
# 2.优化模块名
# 注意：一旦起别名，别名就指向了模块地址，模块名就没有要指向模块地址的必要，那么就失效
```





## 模块的多次导入

```python
# 第一次导入模块，已经完成导入模块的三步，
# 编译=>运行(产生名称空间存放名字)=>执行文件产生名字指向模块的名称空间

# 再次导入：前两步是重复操作，所以只会在当前文件再产生一个名字指向模块的名称空间


# 理由：前两步操作已经将资源放置内存中，从内存中查找速度极高，优先找内存

import m1
import m1
# 相当于：a = 10 | a = 10

import m1
import m1 as m
# 相当于：a = 10 | b = a
```



## 模块在链式导入时的执行流程

```python
# 执行文件.py
print('加载')
import m1  # 进入m1, m1全部走完回到这里
print('结束')

# m1.py
print('m1 开始')
x = 10
import m2  # 进入m2, m2全部走完回到这里
print('m1 结束')

# m2.py
print('m2 开始')
y = 20
print('m2 结束')

'''
加载
m1 开始
m2 开始
m2 结束
m1 结束
结束
'''
# 注：在执行文件中访问20 
print(m1.m2.y)
```





## from...import 语法

```python
# 可以进入模块导具体的名字

from m1 import a
# from导入的三步：
# 前两步同import导入
# 第三步：在执行文件起一个与模块中名字相同的变量指向那个名字的地址：a = m1.a


# 起别名
from m1 import b as bbb  # bbb = m1.b
print(bbb)


# 了了解：不推荐
from m1 import *
# 1）默认将m1中的所有不是以_开头的名字进行导入，在当前执行文件中可以直接使用模块中的名字
# 2）本质导入的是m1模块中__all__管理的名字 ['a', 'b']，被管理的名字可以任意自定义(可以包含_开头)
# 3) 这种方式的导入，名字不能被起别名，一旦发生名字冲突，无法解决


```

## 模块的两种执行方式

#### 自执行

```python
# 在模块中的__name__ = '__main__'
```



#### 作为模块被导入执行

```python
# 在模块中的__name__ = '模块名'
```



#### 共存

```python
# 模块文件

# 先写所有的模块资源(数据 与 函数)
pass

# 模块最下方
if __name__ == '__main__':
    # 自执行的逻辑代码
    pass
```





## 模块的加载顺序

```python
# 内存 > 内置 > sys.path的路径顺序遍历 自定义模块（自己写的，系统写的第三方，别人写的第三方）


# 环境变量: 只是辅助于当前运行的项目，不会影响系统，也不会影响其他项目，所有可以随意操作
import sys
sys.path  # 存放各种模块文件夹路径的列表，可以任意操作来绝对导入自定义模块的顺序
```



## import与from...import:导入的方式采用的是绝对路径

```python
# 绝对路径的依赖：环境变量 sys.path

```



## 环境变量的项目运行

```python
# 在实际开发中，多文件夹之间的模块导入，结构层次杂乱无章，如何规律且准确的进行导包

# 如：项目下part8\a\test.py 导入part8\a\m1.py | part8\a\b\m2.py| part7\c\m3.py
from part8.a import m1
from part8.a.b import m2
from part7.c import m3
# 只需要保证项目目录在环境变量中即可


```

## 项目目录分析

```python
'''
bin: 可执行文件
conf：项目的配置文件
core：项目核心文件，主要的业务逻辑代码
db：数据库相关文件
interface：接口文件
lib：项目的依赖库
log：日志文件
static：静态资源
tmp：临时文件
'''


# 如何将项目所在目录添加至环境变量
# 比如执行文件 项目目录\bin\run.py => 项目目录添加到环境变量的语句
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
```



## 循环导入

```python
# *****

# 问题：彼此相互导入，并使用彼此的名字，如果导入在名字产生之前，就会导致找不到名字，从而出现循环导入错误

# 解决：将名字的产生定义在导入模块之前（延迟导入）

# m1.py
xxx = 666
from m2 import yyy

# m2.py
yyy = 888
from m1 import xxx
```





## 包

```python
# 包:一系列模块的集合体，可以给其他文件提供功能（数据）
# 很多模块的功能相似,将他们统一管理,放在一个文件夹中,该文件夹就称之为 包

# 注：包与普通文件夹不一样，包中必须有__init__文件，py3中可以省略，系统会默认添加，py2中必须手动添加否则报错
```



## 导包

```python
import 包名
import 包名 as 别名

# 导包的三步
# 1) 创建包下__init__文件对应的pyc文件
# 2) 执行__init__文件产生包的名称空间,将__init__文件中的名字放置到包的名称空间中
# 3) 在执行的导包文件中产生一个包名指向包的名称空间 = __init__文件的名称空间

# __init__文件中出现的名字都可以直接用 包名.名字 来使用

# 包m的__init__.py文件
num = 666

# 导包文件
imprt m
print(m.num)



```

##  包的管理

```python
# 1.导包的以.开头的语法，属于包内语法，因为存在.语法开头的导包文件，都不能自执行
# 2.导包的以.开头的语法，只能和 from 结合使用
# 3.在包中的任意模块中都可以使用.语法访问包中其他模块中的名字
# 4.包中.代表当前目录，再添加一个.也就是..代表上一级目录


```









