# coding:utf-8

# 个人博客:https://www.cnblogs.com/Dominic-Ji/p/9278075.html
"""
什么是继承
    继承是一种新建类的方式，继承的类称之为子类或派生类
    被继承的类称之为父类或基类或超类
    子类继承父类，也就意味着子类继承了父类所有的属性和方法
    可以直接调用
为什么要有继承
    减少代码冗余
如何使用
"""
class Parent1:
    pass
class Parent2:
    pass
class Son1(Parent1):
    pass
# python中支持多继承
class Son2(Parent1,Parent2):
    pass
# 如何查看类的父类
# print(Son1.__bases__)
# print(Son2.__bases__)
# 自定义的没有显示继承任何类的父类到底有没有偷偷继承某个类呢？
# print(Parent1.__bases__)
# print(Parent2.__bases__)


"""
python2:类如果没有显示继承任何类的情况下，不继承任何类
python3:类如果没有显示继承任何类的情况下，默认都继承object类

经典类与新式类
   经典类:
        不继承object或者其子类的类  叫经典类  
   新式类: 
        继承object或者其子类的类    叫新式类
ps：经典类与新式类只在python2有区分
python3中只有新式类
"""
# 类:一系列对象相似的特征与技能的结合体
# 类与类之间相似的特征与技能的结合体  >>> 父类
# import pickle
# class OldboyPeople:
#     school = 'oldboy'
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def save(self):
#         with open(self.name,'wb') as f:
#             pickle.dump(self,f)
#
# class OldboyStudent(OldboyPeople):
#     def choose_course(self):
#         print('%s is choosing course'%self.name)
#
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self,name,age,gender,level):
#         OldboyPeople.__init__(self,name,age,gender)
#         self.level = level
#
#     def score(self):
#         print('%s is score'%self.name)



# stu = OldboyStudent('egon',18,'female')
# print(stu.name)
# stu.save()

# tea = OldboyTeacher('jason',18,'male',10)
# print(tea.name)
# tea.save()

# 派生:在继承了父类的属性和方法的基础之上 自己定义了其他的属性和方法
# 如果派生出的方法与父类的同名了 那么相当于覆盖了父类的方法


# 子类方法中调用父类的方法
# 方式1:指名道姓
# OldboyPeople.__init__(self,name,age,gender)   跟继承一毛钱关系都没有

# 方式2:跟继承有关系？


# 单继承情况下的属性查找
# class B:
#     def f1(self):
#         print('from B f1')
#
#     def f2(self):
#         print('from B f2')
#         self.f1()
# class A(B):
#     def f1(self):
#         print('from A f1')
# obj = A()
# obj.f2()
"""
猜测结果(大)
from B f2
from B f1
猜测结果(小)
from B f2
from A f1
"""

# 多继承
# class D:
#     # def test(self):
#     #     print('D')
#     pass
# class E:
#     def test(self):
#         print('E')
# class F:
#     def test(self):
#         print('F')
# class A(D):
#     # def test(self):
#     #     print('A')
#     pass
# class B(E):
#     # def test(self):
#     #     print('B')
#     pass
# class C(F):
#     def test(self):
#         print('C')
# class G(A,B,C):
#     # def test(self):
#     #     print('G')
#     pass
#
# obj = G()
# obj.test()
# 无论是python2还是python3继承都遵循深度优先(菱型继承除外)
# class C:
#     def test(self):
#         print('C')
# class A(C):
#     # def test(self):
#     #     print('A')
#     pass
# class B(C):
#     def test(self):
#         print('B')
# class G(A,B):
#     # def test(self):
#     #     print('G')
#     pass
# obj = G()
# obj.test()


# import pickle
# class OldboyPeople:
#     school = 'oldboy'
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def save(self):
#         with open(self.name,'wb') as f:
#             pickle.dump(self,f)
#
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self,name,age,gender,level):
#         # OldboyPeople.__init__(self,name,age,gender)
#         # super(OldboyTeacher,self).__init__(name,age,gender)
#         super().__init__(name,age,gender)
#         self.level = level
# tea = OldboyTeacher('jason',18,'male',10)
# print(tea.name)
# tea.save()

# mro列表   C3算法
class D:
    pass
class E:
    pass
class F:
    pass
class A(D):
    pass
class B(E):
    pass
class C(F):
    pass
class G(A,B,C):
    pass
"""
G A D B E C F
[<class '__main__.G'>, <class '__main__.A'>, <class '__main__.D'>, 
<class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, 
<class '__main__.F'>, <class 'object'>]

"""
# print(G.mro())
# # super是严格按照mro列表的顺序调用父类的方法的！！！
# class A:
#     def f1(self):
#         print('from a f1')
#     def f2(self):
#         print('from a f2')
#         super().f1()
# class B:
#     def f1(self):
#         print('from b f1')
#     def f2(self):
#         print('from b f2')
# class C(A,B):
#     def f1(self):
#         print('from c f1')
# print(C.mro())
# # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# obj = C()
# obj.f2()

# from datetime import datetime,date
# import json
# # d ={'name':'jason','password':'123'}
# res = {"t1":datetime.today(),'t2':date.today()}
# class MyCustomerJson(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o,datetime):
#             return o.strftime('%Y-%m-%d %X')
#         elif isinstance(o,date):
#             return o.strftime('%Y-%m-%d')
#         else:
#             return super().default(self,o)
# print(json.dumps(res,cls=MyCustomerJson))
# TypeError: Object of type 'datetime' is not JSON serializable



# 多态与多态性
"""
什么是多态
    一种事物的不同形态(动物:人，狗，猫)，代码层面上来说其实就是继承      
为什么要有多态
    多态仅仅是一个概念
    多态性:在不需要考虑对象具体类型的情况下 调用对象的方法    
如何使用
"""
# class Animal:
#     def talk(self):
#         pass
# class People(Animal):
#     def talk(self):
#         print('hello')
# class Dog(Animal):
#     def talk(self):
#         print('wangwang')
# class Cat(Animal):
#     def talk(self):
#         print('miaomiao')
# people = People()
# dog = Dog()
# cat = Cat()
#
# people.talk()
# dog.talk()
# cat.talk()


# l = [1,2,3,4,5]
# t = (1,2,3,4,5)
# s = 'hello'
# # 只要是容器类型
# print(len(l))
# print(len(t))
# print(len(s))

# 多态性能够实现的基础是什么
# class Animal:
#     def talk(self):
#         pass
# class People(Animal):
#     def jiao(self):
#         print('hello')
# class Dog(Animal):
#     def wang(self):
#         print('wangwang')
# class Cat(Animal):
#     def miao(self):
#         print('miaomiao')
# p = People()
# d = Dog()
# c = Cat()
#
# p.talk()
# d.talk()
# c.talk()
# import abc
# class Animal(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def talk(self):
#         pass
#
# class People(Animal):
#     def talk(self):
#         print('hello')
# class Dog(Animal):
#     def wang(self):
#         print('wangwang')
# class Cat(Animal):
#     def miao(self):
#         print('miaomiao')
# people = People()

# from functools import wraps
# def outer(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         return func(*args,**kwargs)
#     return inner
#
# @outer  # func = outer(func)
# def func():
#     pass
#
# print(func)

# class People:
#     def talk(self):
#         pass
# class Dog:
#     def talk(self):
#         pass
# class Cat:
#     def talk(self):
#         pass

# python推崇鸭子类型
# 只要你长得像鸭子 走路像鸭子 说话像鸭子 那么你就是鸭子


# linux一切皆文件
# class Disk:
#     def read(self):
#         pass
#     def write(self):
#         pass
# class Memory:
#     def read(self):
#         pass
#     def write(self):
#         pass
# class Process:
#     def read(self):
#         pass
#     def write(self):
#         pass

# 类:
# 写面条版程序
# 写函数版本的程序
# 面向对象编程


















