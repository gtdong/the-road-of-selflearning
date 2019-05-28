# 今日内容

面向对象的三大特性

* 封装
* 继承与派生
* 多态与多态性

绑定方法与非绑定方法

内置的方法

元类

异常处理


# 1.继承与派生

#### 1.什么是继承

继承就是一种新建类的方式,新建的类称为子类或者派生类，被继承的类称之为父类或者基类或者超类

子类会继承所有父类的属性和方法，即可以直接使用这些属性和方法

#### 2.为什么要用继承

减少代码冗余

#### 3.如何使用

```python
class Parent1:
  pass
class Parent2:
  pass
class Son1(parent1):
  pass
# python支持多继承，一个类可以有多个父类，但在java中只能有一个
class Son2(parent1,parent2):
  pass
print(Son1.__bases__)  # 查看当前类的所有的基类
print(Son2.__bases__)  

# 那你是否会好奇想看看我们定义的Parent类它有没有偷偷摸摸的继承谁呢？
print(Parent1.__bases__)
print(Parent2.__bases__)

# 切换python解释器3.x >>> 2.x得出一个结论
"""
在python3中，如果没有显示地继承任何类，那默认继承object类
在python2中，如果没有显示地继承任何类，也不会继承object类


在python中类分为两种：
        新式类:
            但凡继承object的类，或者该类的子类都是新式类
            >>>:在python3中所有的类都是新式类
        经典类
            没有继承object类，以及该类的子类都是经典类
            也就意味着经典类和新式类这对儿概念只在python2中有
            python3中只有新式类
"""
```

#### 4.基于继承减少代码冗余的案例+派生/衍生

对象与对象之间总结相似的特征与技能得到类
类与类之间总结相似的属性和特征得到父类

<http://www.cnblogs.com/linhaifeng/articles/7340153.html>

```python
# 代码实例
import pickle

class OldboyStudent:
    school = 'oldboy'

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def choice_course(self):
        print('%s is choosing course'%self.name)

    def save(self):
        with open(self.name,'wb') as f:
            pickle.dump(self,f)

class OldboyTeacher:
    school = 'oldboy'

    def __init__(self,name,age,sex,level):
        self.name = name
        self.age = age
        self.sex = sex
        self.level = level

    def score(self):
        print('%s is score'%self.name)

    def save(self):
        with open(self.name,'wb') as f:
            pickle.dump(self,f)
stu = OldboyStudent('alex',30,'male')
stu.save()

tea = OldboyTeacher('egon',18,'male',10)
tea.save()

# 回过头来看，上面的代码是否存在相似的部分。我们刚好学过解决类之间解决代码冗余的方式
class OldboyPeople:
    school = 'oldboy'

    def save(self):
        with open(self.name, 'wb') as f:
            pickle.dump(self, f)
# 初步继承类抽取，思考继承之后对象查找属性和方法的顺序
stu.save()
stu.school

# 刚刚只是讲属性和方法抽成了父类，但是init里面也有重复的代码，应该也可以抽取
class OldboyPeople:
    school = 'oldboy'
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def save(self):
        with open(self.name, 'wb') as f:
            pickle.dump(self, f)
# 先不考虑老师和学生init中不同的，先全部继承这个父类统一的init，发现也可以使用到父类的init

# 派生概念
# 在子类能够使用父类所有的属性和方法的同时，自身还有一些额外的属性和方法
# 小思考:如果派生的属性和方法恰巧和父类的一样，那在查找属性和方法的时候先找到谁呢？ >>> 还是按查找顺序来

# 再回过头来看老师的init中有额外的level参数，不应该在父类中添加默认参数，只能自己重写init方法，但是又有重复的代码出现
    def __init__(self,name,age,sex,level):
        OldboyPeople.__init__(self,name,age,sex)
        self.level = level
"""
在子类派生出的新方法中重用父类的方法
方式1:指名道姓访问，与继承没有任何关系
OldboyPeople.__init__(self,name,age,sex)
言外之意还有一种跟继承有关系的能够重用父类的方法的方式，先不着急说
"""
```

#### 5.继承原理

刚刚我们一直在讨论的是单继承下属性查找的顺序，那如果是多继承情况呢？

单继承测试

```python
class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self): #self=obj
        print('Foo.f2')
        self.f1() #obj.f1()

class Bar(Foo):
    def f1(self):
        print('Bar.f1')


obj=Bar()
obj.f2()
```

多继承

```python
# F(A,B,C) 无论是新式类还是经典类，都是从左往右挨个走到底 画图 切换python版本演示，记得加文件头coding:utf-8
# 2、多继承的属性查找“：对象自己-》对象的类-》从左往右一个一个的分支找下去
class D:
    # def test(self):
    #     print('D')
    pass
class E:
    def test(self):
        print('E')

class F:
    def test(self):
        print('F')

class A(D):
    # def test(self):
    #     print('A')
    pass

class B(E):
    def test(self):
        print('B')

class C(F):
    def test(self):
        print('C')

class G(A,B,C):
    # def test(self):
    #     print('G')
    pass

obj=G()
obj.test()
```

如果是菱型继承的话就不一样了(不考虑object)>>>广度优先!

```python
#3、新式类：广度优先
class A(object):
    def test(self):
        print('from A')
class B(A):
    # def test(self):
    #     print('from B')
    pass
class C(A):
    # def test(self):
    #     print('from C')
    pass
class D(B):
    # def test(self):
    #     print('from D')
    pass
class E(C):
    # def test(self):
    #     print('from E')
    pass
class F(D,E):
    # def test(self):
    #     print('from F')
    pass

obj=F()
print(F.mro())  # 查找属性的顺序遵循mro列表(只有新式类中才有mro方法)
obj.test()
```

回过头再来看通过继承关系调用父类的方法

```python
# 方式二：super(自己的类名,self).父类中的方法名()
# 调用super会得到一个特殊的对象，该对象是专门用来引用父类中的方法的，
# 具体的：该对象会严格按照当前类的MRO列表从当前类的父类中依次查找属性，即这种方式是严格依赖于继承的
# ps:在python3中可以简写为super()
class OldboyPeople:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,level):
        # OldboyPeople.__init__(self,name,age,sex)
        super(OldboyTeacher,self).__init__(name,age,sex)
        self.level=level

tea1=OldboyTeacher('egon',18,'male',10)
print(tea1.name,tea1.level)


class A:
    def f1(self):
        print('A')
        super().f2() # super（）会基于当前所在的查找位置继续往后查找
    def f2(self):
        print('A')
class B:
    def f2(self):
        print('B')
class C(A,B):
    def f2(self):
        print('C')

obj=C()
print(C.mro())
obj.f1()
```

实际工作中要谨慎使用多继承，编程是解耦合，而继承则是强耦合





#### 6.多态与多态性

1.什么是多态

​	同一种事物的多种形态(动物:人，猫，狗)

2.为何要用多态

​	多态性:指的是可以在不用考虑对象具体类型的前提下，直接调用对象的方法

3.如何使用多态

```python
class Animal:
    def talk(self):
        pass

class People(Animal):
    def talk(self):
        print('say hello')

class Dog(Animal):
    def talk(self):
        print('汪汪汪')

class Pig(Animal):
    def talk(self):
        print('哼哼哼')

peo1=People()
dog1=Dog()
pig1=Pig()

# 不用考虑对象具体类型的前提下，直接调用对象的方法
peo1.talk()
dog1.talk()
pig1.talk()
"""
再来想车是不是有很多牌子，你去学车需要说专门学哪个牌子的车的驾驶方式吗？
"""
# 来你之前也一直在用多态性:不用考虑对象具体类型的前提下，直接调用对象的方法
l=list([1,2,3])
s=str('hello')
t=tuple((4,5,6))

l.__len__()
s.__len__()
t.__len__()  # 我不需要考虑这三个具体是什么类型，只要是容器类型就都能调用len这个方法

# 再来看多态性能够实现的条件是什么？父类有的方法名子类也必须叫这个方法才行
class Animal:
    def talk(self):
        pass

class People(Animal):
    def jiao(self):
        print('say hello')

class Dog(Animal):
    def han(self):
        print('汪汪汪')

class Pig(Animal):
    def hou(self):
        print('哼哼哼')
# 多态性能实现的条件就是父类给子类定义了一个标准，动物都必须会叫，并且叫的方法都必须是talk
# 但是你现在能约束我说子类必须叫这个方法吗？

# 那有没有一种情况能够做到说子类必须按照父类定义的标准
import abc
class Animal(metaclass=abc.ABCMeta): # 父类存在的意义就是用来定义规范
    @abc.abstractmethod
    def talk(self):
        pass

# Animal() # 抽象基类不能被实例化！！！
class People(Animal):
    def jiao(self):
        print('say hello')
class Dog(Animal):
    def han(self):
        print('汪汪汪')
class Pig(Animal):
    def hou(self):
        print('哼哼哼')
# 上面三个类 一实例化都会报错

# 但是python推崇的是自由，简约并不希望限制程序员的开发
# 鸭子类型：只要你长得像鸭子，说话像鸭子，那你就是鸭子！
class People:
    def talk(self):
        print('say hello')
class Dog:
    def talk(self):
        print('汪汪汪')
class Pig:
    def talk(self):
        print('哼哼哼')

# 再来看linux中:一切皆文件！
class Disk:
    def read(self):
        print('disk read')
    def write(self):
        print('disk write')
class Process:
    def read(self):
        print('process read')
    def write(self):
        print('processes write')
class Memory:
    def read(self):
        print('memory read')
    def write(self):
        print('memory write')
```

#### 7.类中的装饰器

```python
# property
# 人体的BMI指数
"""
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）/ 身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
"""
class People:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)


egon=People('egon',1.80,75)
egon.height=1.82
# print(egon.bmi())

print(egon.bmi)



# 了解
class People:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,val):
        # print('=====>准备修改名字的值：',val)
        if type(val) is not str:
            raise TypeError('名字的值必须为str类型')
        self.__name=val

    @name.deleter
    def name(self):
        # del self.__name
        print('不让删啊老铁')
 
# classmethod

# staticmethod
```

#### 8.反射

通过字符串来获取类或对象的属性或方法

```python
#1、反射：指的是通过字符串来操作类或者对象的属性
class People:
    country='China'
    def __init__(self,name):
        self.name=name


obj=People('egon')


#涉及四个内置函数
# hasattr
print('country' in People.__dict__)
print(hasattr(People,'country'))

# getattr
print(People.__dict__['country'])
print(getattr(People,'country'))
print(getattr(People,'country1111',None))

# setattr
People.__dict__['x']=111
print(People.x)
setattr(People,'x',111)
print(People.__dict__)

# delattr
delattr(People,'country')
print(People.__dict__)


# 应用
class Ftp:
    def get(self):
        print('get...')

    def put(self):
        print('put...')

    def auth(self):
        print('auth...')

    def run(self):
        while True:
            cmd=input('>>: ').strip() #cmd='get'
            if hasattr(self,cmd):
                method=getattr(self,cmd)
                method()
            else:
                print('输入的方法不存在')
obj=Ftp()
obj.run()
```

#### 9.内置方法

```python
# __str__
# __getattr__  注意是对象获取自己没有的属性时才会触发(属性和方法)
# __setattr__
```

#### 10.元类

<https://www.cnblogs.com/Dominic-Ji/p/10520256.html>

# 异常处理

#### 1.什么是异常？

异常是错误发生的信号，程序一旦出错，如果程序中还没有相应的处理机制，那么该错误就会产生一个异常抛出来，程序的运行也随之终止

```python
print('start')
x = 1
y = 2
if 
print('end')  # 程序一句也不会运行直接报错，运行前会先检测语法
```

异常分为三部分：
        异常的类型(一个个的类)
        异常的内容、提示信息
        异常的追踪/定位信息信息

异常的分类:

* 语法上的错误(如上例)

* 逻辑上的错误

  ```python
  # NameError
  age = 12
  a
  # IndexError
  l = [1,2,3]
  l[123]
  # KeyError
  d = {'name':'jason'}
  d['password']
  ```

#### 2 为何要进行异常处理

​    增强程序的健壮性

#### 3 如何进行异常处理

```python
try
	...
except
	...
```

```python
#针对逻辑上的异常才应该使用try...except去捕捉异常进行处理
#1、异常的单分支(单个except)
#2、异常的多分支(多个except)
#3、万能异常：Exception，可以匹配所有种类的异常(挨个注释挨个尝试)
try:
     age
     l=[1,2,3]
     l[100]
     d={'x':1}
     d['y']
     import os
      os.xxx
except Exception as e:  # as语法将错误信息赋值给变量e
     print('万能异常')
		 print(e)  
print('其他代码')
#4、多分支+Exception，注意Exception一定要放到except 其他异常的的后面
#5、try...else，else会在被检测的代码块没有异常发生的情况下执行， else一定要与except连用，并且一定要放到多个except后面
#6、try...finally,finally的代码，无论被检测的代码有无异常，都会执行，通常在finally内做一些回收资源的事情
try:
  f = open('a.txt','w',encoding='utf-8')
  f.read()
finally:
  f.close()
print('other...')
#7、主动触发异常raise 异常类型(’异常的内容‘)
# 应用于程序中自定义某种法则，一旦不遵循则会像抛出语法异常一样，终止程序的运行
class People:
  def __init__(self,name):
    if not isinstance(name,str):
      raise TypeError('%s must be str type'%name)
     self.name = name

#8、断言
l = [1,2,3]
assert len(l) > 0

#9 自定义异常
class MyError(BaseException):
     def __init__(self,msg):
         super().__init__()
         self.msg=msg
     def __str__(self):
         return '<%s>' %self.msg

raise MyError('我自己定义的异常')  # 主动抛出异常其实就是将异常类的对象打印出来,会走__str__方法
```













