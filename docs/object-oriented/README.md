## 面向对象编程
### 1.什么是面向对象
    面向过程与面向对象
        面向过程编程：解决问题从过程出发，解决问题步骤化

        面向对象编程：解决问题从对象出发，解决问题找对象

    对象与类
        类：对象的类型 => 数字
            具有相同特征与行为集合的抽象

        对象：类的具体表现 => 数字10
            类的实例化，就是具有特征与行为实际存在的个体（每一个对象都是唯一的）

### 2.为什么要面向对象编程
    面向过程：开发成本高，解决问题局限性小
    面向对象：开发成本低，解决问题局限于对象

    问题：'abc' => {'a', 'b', 'c'}
         面向过程: 手撸
         面向对象：str => list => set

    开发：优选面向对象(找解决问题的对象)，
    再考虑找多个对象(面向对象与面向过程的结合)，
    最后自己去封装一个可以解决问题的对象(对外是面向对象的体现，内部解决问题的核心是面向过程)

### 3.引子

```python
# 需求
s = 'abc'  # => ['a', 'b', 'c']
# 解决方案
# re.findall()  list初始化方法
# for循环append

# 面向过程：解决问题步骤化
res = []
for c in s:
    res.append(c)
print(res)

# 面向对象：解决问题找对象
#       -- 对象如何解决问题：对象.解决问题的方法()

# 找re对象
import re
res = re.findall(r'[a-z]', s)
print(res)

# 找list对象
res = list(s)
print(res)
```



## 类的声明语法

```python
class 类名:
    # 在该缩进下(在类下)定义多个函数，类名就可以整体管理所有的函数，通过点语法来调用具体的函数
    def fn1():
        print('fn1 run')
    def fn2():
        print('fn2 run')
    def fn3():
        print('fn3 run')
        
# 类名的命名规范：采用大驼峰
```



## 点语法与名称空间

```python
# 可以产生名称空间的语法

def fn():  # 具有名称空间：fn.__dict__
    pass

class Fn():  # 具有名称空间：Fn.__dict__
    pass

import md  # 具有名称空间：md.__dict__


# 名称空间如何为一个名字设置值，或访问一个名字对应的值
fn.__dict__[名字] = 值  # 设置值
print(fn.__dict__[名字])  # 取值


# 重点：名称空间取值赋值的语法优化：点语法
fn.名字 = 值  # 设置值
print(fn.名字)  # 取值
```



## 类与对象的声明

```python
class People:
    name = '人'
    
p1 = People()
p2 = People()

# 结论1：类与每一个对象的名称空间都是独立的
print(p1.__dict__)  # {}
print(p2.__dict__)  # {}
print(People.__dict__)  # {'name': '人', ...系统的}

# 结论2：类与每一个对象都可以使用类中的名字
print(People.name)  # 人
print(p1.name)  # 人
print(p2.name)  # 人

# 结论3：对象访问名字，优先访问自己的，自己没有再访问类的
p1.name = '张三'
p2.user = '李四'
print(People.name)  # 人
print(p1.name)  # 张三
print(p2.user)  # 李四
print(p2.name)  # 人

# 重点：
# 对象操作名字，操作的是对象的，类操作名字操作的是类的，之间相互不干预
# 类只能访问类的名字
# 对象访问名字，优先访问自身的，自身没有再访问类的
```



## 类的初始化方法

```python
# 可以快速为类实例化出的每一个对象，产生对象名称空间中的多个名字

class NewTeacher:
    def __init__(self, name, sex, age):
        # print(id(self))  # self就是实例化产生的对象(nt1)
        # print('init 被调用了')
        self.name = name
        self.sex = sex
        self.age = age
    pass

# 类()就是在调用类的__init__方法
nt1 = NewTeacher('王大锤', '男', 58)
# print(id(nt1))
print(nt1.name, nt1.sex, nt1.age)


nt2 = NewTeacher('王小锤', '男', 48)
print(nt2.name, nt2.sex, nt2.age)
```



## 类的方法分类

```python
"""
# 对象方法：直接定义的方法，建议由对象调用，类中内部需要使用对象的数据时的方法要定义为对象方法
# 1.对象方法对象调用，默认传入对象给第一个形参 
class 类名:
    def fn(self, *args, **kwargs): pass

# 类方法：被classmethod修饰的方法，建议由类调用，类中内部需要使用类的数据时的方法要定义为类方法
# 2.类方法由类调用，默认传入类给第一个形参
class 类名:
    @classmethod
    def fn(cls, *args, **kwargs): pass

# 静态方法：被staticmethod修饰的方法，建议由类调用，类中内部不需要类相关数据时的方法要定义为静态方法
# 3.静态方法建议由类调用，默认不传入调用者
    @staticmethod
    def fn(*args, **kwargs): pass
"""
```

```python
# 案例
class Book:
    name = '书'
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 书的详情信息 => 一定需要知道哪本书
    # @classmethod  # 类调用cls就是类，对象调用处理成 对象.__class__

    def detail(self):
        # print(cls.name)
        print("%s的价格为:%s元" % (self.name, self.price))

book1 = Book('西游记', 38.8)
book2 = Book('金瓶梅', 88.8)
book1.detail()
book2.detail()
# print(book1.__class__)


# 静态方法：方法的内部不需要对象及类的参与，所以定义为静态方法，但是方法必须由调用者，建议用类就可以了
class NumTool:  # 工具类 => 模块
    def max_two(self, n1, n2):
        max_num = n1 if n1 > n2 else n2
        print('大数是%s' % max_num)

    @staticmethod
    def new_max_two(n1, n2):
        max_num = n1 if n1 > n2 else n2
        print('大数是%s' % max_num)

n1 = NumTool()
n2 = NumTool()
n1.max_two(10, 20)
n2.max_two(10, 20)

NumTool.new_max_two(10, 20)
n1.new_max_two(10, 20)


# 类方法：方法的内部需要类的参与，所以定义为类方法，第一个参数默认传类
class NewNumTool:
    PI = 3.14

    @classmethod
    def new_max_two(cls, n1, n2):
        max_num = n1 if n1 > n2 else n2
        return max_num

    @classmethod
    def new_max_three(cls, n1, n2, n3):
        # max_num = "想去复用new_max_two"
        max_num = cls.new_max_two(n1, n2)
        max_num = cls.new_max_two(max_num, n3)
        return max_num

    @classmethod
    def is_PI(cls, num):
        if num == cls.PI:
            return True
        return False


res = NewNumTool.new_max_three(1, 5, 3)
print('大数是%s' % res)

print(NewNumTool.is_PI(3.149))
```





## 类的三大特性

#### 封装

```python
# 什么是封装：将类的一下属性和方法对外隐藏，对内可见
# 为什么要封装：为属性和方法的操作添加权限，具体权限都是通过自定义逻辑来处理


# 封装的手段：在类属性方法，对象属性方法，静态方法名字前添加 __
# 只要是通过 __名字 这种命名规范，就是对外隐藏
    # 本质：__名字 封装隐藏变量的本质是 将名字修饰成 _类名__名字
    
# 对外解决封装的方式
# 1.如果真的不想让外界访问，就不对外提供访问数据的方法
# 2.如果想让外界访问，可以对外提供访问数据的方法，方法具有逻辑，使用可以添加操作权限
class Test:
    def __init__(self, name):
        # __name只是对外隐藏，对内可见
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if 'sb' not in name:  # 对数据的修改可能会产生数据的安全性问题，可以添加限制条件
            self.__name = name

            
# 重点：封装的对外访问语法的优化
class User:
    def __init__(self, name):
        self.__name = name

    @property  # 将方法伪装成属性
    def name(self):
        return self.__name

    @name.setter  # 能为有伪装get方法的(方法)属性，再伪装set方法
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name
        
    # 总结：
    # 1.对象没了，对象的属性也就没了，所以不需要属性 @名字.deleter
    # 2.对外提供get方法是基础，@property，如果没有，外界不可读不可写
    # 3.如果有@property，则可以 @名字.setter，有set，为可读可写，无set为只读

    @property  # 伪装的属性方法，不需要一定有 __开头 的名字与之对应
    def pwd(self):
        return '123456'

u1 = User('Owen')
print(u1.name)  # 如果一个方法伪装成属性，对象.方法名 就会自动调用该方法

u1.name = 'Zero'
print(u1.name)

# del u1.name
# print(u1.name)

print(u1.pwd)
```



