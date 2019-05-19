## 面向对象

```python
''''
1、面向过程编程
    核心是"过程"二字，过程指的是解决问题的步骤，即先干什么再干什么
    基于该思想编写程序就好比在编写一条流水线，是一种机械式的思维方式

    优点：复杂的问题流程化、进而简单化
    缺点：可扩展性差

2、面向对象
    核心"对象"二字，对象指的是特征与技能的结合体，
    基于该思想编写程序就好比在创造一个世界，你就是这个世界的上帝，是一种
    上帝式的思维方式

    优点：可扩展性强
    缺点：编程的复杂度高于面向过程
    
重点：面向对象的核心体现是将数据和处理数据的程序封装到对象中
'''
```

#### 名称空间操作

```python
import re
print(re.__dict__)

def fn():
    pass
print(fn.__dict__)
```

#### 类与对象

```python
# 类：具有相同特征与行为事物集合体的抽象
# 对象：现实中，实际存在的各个事物，也就是抽象出的类的具体表现

# 定义类
class Student:
    pass

# 产生对象
stu = Student()

# 添加特征与行为
stu.name = 'Owen'
stu.get_age = lambda age: age
```

#### 初始化方法

```python
class Student:
    def __init__ (self, name):
        self.name = name
```

#### 属性的查找顺序

```python
class Student:
    school = "Oldboy"
    def __init__ (self, name):
        self.name = name
```

#### 对象方法与类方法

```python
class Student:
    school = "Oldboy"
    def __init__ (self, name):
        self.name = name
        
    def study(self):
        print(self.name + '学习')
        
    @classmethod
    def school_time(cls):
        print('8点半')
```



## 面向对象三大特性：封装、继承、多态

#### 封装

```python
# 封装：对外隐藏对象的属性与功能的实现细节

# 优点：保证数据的安全性

# 应对措施：对外提供安全的操作结构，外部仍然可以通过接口来操作对象的属性
```

#### 私有化

```python
class Student:
    __identity = '学生'
    def __init__(self, id, name):
        self.__id = id  # 将id设置为私有的
        self.name = name
```

#### 功能的私有化

```python
class Student:
    __identity = '学生'
    def __init__(self, id, name):
        self.__id = id  # 将id设置为私有的
        self.name = name
        
    # 仅供内部使用的函数
    def __test():
        print('仅供内部使用的函数')
```

#### 对外提供接口

```python
class Student:
    def __init__(self, id, name):
        self.__id = id  # 将id设置为私有的
        self.name = name
        
        @property
        def id(self):
            return self.__id

        @id.setter
        def id(self, value):
            self.__id = value

        @id.deleter
        def id(self):
            del self.__id
```



#### 组合：自定义类的对象作为自定义类的属性

```python
class Teacher:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, id, name, teacher):
        self.__id = id  # 将id设置为私有的
        self.name = name
        self.teacher = teacher
        
t = Teacher('Tom')
s = Student(1, 'Bob', t)
print(s.teacher.name)
```



## 继承

```python
# 继承：子类与父类形成的一种关系，可以让子类能直接从父类中获取属性与方法

# 优点：减少代码冗余
```

#### 语法

```python
class Sup:
    pass
class Sub(Sup):
    pass
```

#### 属性与方法的继承

```python
# 父类所有非封装的属性和方法都可以被继承
```

#### 有父类时的属性(方法)查找顺序

```python
class Sup:
    num = 10
    def test(self):
        print('sup test')
class Sub(Sup):
    num = 10
    def test(self):
        print('sub test')
# 子类优先使用自身的属性和方法
```

#### 子类重写父类方法

```python
# 由于属性查找顺序，所以子类可以重写父类的方法
```

#### 子类重用父类方法

```python
# 子类中利用super(子类名, 当前子类对象)可以调用父类的方法
# Python3中可以简写super()
```

#### 经典类与新式类

```python
# 经典类：Python2中没有明确继承关系的类(没有直接或间接基础object的类)
# 新式类：没有直接或间接基础object的类(Python3中没有明确继承关系的类默认继承object)
```

#### 多继承的属性查找顺序

```python
# 菱形继承下
# 经典类：采用深度优先查找方式
# 新式类：采用广度优先查找方式
```



## 接口

```python
# 提供功能说明的，Python中没有接口的语法
```



## 抽象类

```python
# 利用abc模块实现抽象类
import abc 
class ABC_Sup(metaclass=abc.ABCMeta):
    # 定义抽象方法，无需实现功能，继承抽象类的子类必须实现该方法
    @abc.abstractmethod 
    def read(self):
        pass
```



## 多态

```python
# 事物的多种形态

# 1.利用继承关系形成的多态
# 2.利用鸭子类型形成的多态
```



## 接口

```python
# 提供功能说明的，Python中没有接口的语法
```



## 抽象类

```python
# 利用abc模块实现抽象类
import abc 
class ABC_Sup(metaclass=abc.ABCMeta):
    # 定义抽象方法，无需实现功能，继承抽象类的子类必须实现该方法
    @abc.abstractmethod 
    def read(self):
        pass
```



## 多态

```python
# 事物的多种形态

# 1.利用继承关系形成的多态
# 2.利用鸭子类型形成的多态
```



## 内置方法

```python
# 格式化：__str__()
# 析构：__del__()

# 了解：__setattr__()、__setitem__()
```



## 反射

```python
# 反射：通过字符串与类及类的对象的属性建立关联
'''
setattr
getattr
hasattr
delattr
'''
```



## 异常

```python
# 程序运行时的错误

'''
异常三部分信息：
	1.追踪信息
	2.类型
	3.值
	
异常处理结构：
try:
	# 会出现异常的代码块
except 异常类型 as 异常别名:
	# 异常处理逻辑
else:
    # 没有出现异常会执行该分支
finally:
    # 无论是否出现异常都会执行该分支

主动抛出异常
raise 异常类型('异常信息')

自定义异常类：
class MyError(BaseException):
    def __init__(self, msg):
        self.msg = msg
        
断言：
assert 断言条件
'''


```

| 异常名称                  | 描述                                               |
| ------------------------- | -------------------------------------------------- |
|                           |                                                    |
| BaseException             | 所有异常的基类                                     |
| SystemExit                | 解释器请求退出                                     |
| KeyboardInterrupt         | 用户中断执行(通常是输入^C)                         |
| Exception                 | 常规错误的基类                                     |
| StopIteration             | 迭代器没有更多的值                                 |
| GeneratorExit             | 生成器(generator)发生异常来通知退出                |
| StandardError             | 所有的内建标准异常的基类                           |
| ArithmeticError           | 所有数值计算错误的基类                             |
| FloatingPointError        | 浮点计算错误                                       |
| OverflowError             | 数值运算超出最大限制                               |
| ZeroDivisionError         | 除(或取模)零 (所有数据类型)                        |
| AssertionError            | 断言语句失败                                       |
| AttributeError            | 对象没有这个属性                                   |
| EOFError                  | 没有内建输入,到达EOF 标记                          |
| EnvironmentError          | 操作系统错误的基类                                 |
| IOError                   | 输入/输出操作失败                                  |
| OSError                   | 操作系统错误                                       |
| WindowsError              | 系统调用失败                                       |
| ImportError               | 导入模块/对象失败                                  |
| LookupError               | 无效数据查询的基类                                 |
| IndexError                | 序列中没有此索引(index)                            |
| KeyError                  | 映射中没有这个键                                   |
| MemoryError               | 内存溢出错误(对于Python 解释器不是致命的)          |
| NameError                 | 未声明/初始化对象 (没有属性)                       |
| UnboundLocalError         | 访问未初始化的本地变量                             |
| ReferenceError            | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
| RuntimeError              | 一般的运行时错误                                   |
| NotImplementedError       | 尚未实现的方法                                     |
| SyntaxError               | Python 语法错误                                    |
| IndentationError          | 缩进错误                                           |
| TabError                  | Tab 和空格混用                                     |
| SystemError               | 一般的解释器系统错误                               |
| TypeError                 | 对类型无效的操作                                   |
| ValueError                | 传入无效的参数                                     |
| UnicodeError              | Unicode 相关的错误                                 |
| UnicodeDecodeError        | Unicode 解码时的错误                               |
| UnicodeEncodeError        | Unicode 编码时错误                                 |
| UnicodeTranslateError     | Unicode 转换时错误                                 |
| Warning                   | 警告的基类                                         |
| DeprecationWarning        | 关于被弃用的特征的警告                             |
| FutureWarning             | 关于构造将来语义会有改变的警告                     |
| OverflowWarning           | 旧的关于自动提升为长整型(long)的警告               |
| PendingDeprecationWarning | 关于特性将会被废弃的警告                           |
| RuntimeWarning            | 可疑的运行时行为(runtime behavior)的警告           |
| SyntaxWarning             | 可疑的语法的警告                                   |
| UserWarning               | 用户代码生成的警告                                 |

