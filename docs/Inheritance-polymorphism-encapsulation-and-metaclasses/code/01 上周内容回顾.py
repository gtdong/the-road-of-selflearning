"""
继承
多态与多态性

面向对象高级
装饰器
内置方法
反射(******)

元类

单例模式


异常处理
"""

# 上周内容回顾
"""
 常用模块
    time与datetime
    os
    sys
    json与pickle
    random
    re
 面向对象
"""
# import time
# from datetime import datetime
# print(time.time())
# print(time.strftime('%Y-%m-%d %X'))
# print(datetime.now())
# print(datetime.today())

# import os
# import sys
# print(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(__file__)
# sys.path.append(BASE_DIR)


# 对数据的》》》增删改查
# import json


# import random
# random.randint(1,9)
# random.choice([1,2,3])
# l = [1,2,3,4,5,6]
# random.shuffle(l)
# print(l)

# 生成随机验证码
# import random
# code = ''
# for i in range(4):
#     code_1 = str(random.randint(1,9))
#     code_2 = chr(random.randint(65,90))
#     code_3 = chr(random.randint(97,122))
#     code += random.choice([code_1,code_2,code_3])
# print(code)
# res = 'vftc'
# print(code.upper())
# if code.upper() == res.upper():
#     pass


import re
"""
贪婪匹配与非贪婪匹配
.*
.*?
"""


# 面向对象
"""
    面向过程编程
        面向过程编程，核心是过程二字，过程就是解决问题的步骤 即先干什么再干什么最后干什么
        基于该思想编程就好比在造一条流水线
        优点:复杂的问题流程化从而简单化
        缺点:可扩展性较差
    
    面向对象编程
        面向对象编程 核心是对象二字 对象即一系列相似的特征与技能的集合体
        基于改思想编写程序就好比在创造一个世界，程序员就是这个世界的造物主
        在造物主眼里一切皆对象
        优点:可扩展性高
        缺点:较于面向过程变成难度较高
"""
# 定义一个类
# 什么是类？:一系列对象相似的特征与技能的结合体
# class User:
#     school = 'oldgirl'
#     def __init__(self,name):
#         self.name = name
#     def func(self):
#         pass
# 类你可以理解为就一个容器， 将产生的一堆名字放到这个容器中
# print(User.__dict__)
# print(User.__dict__['school'])
# print(User.__dict__['func'])
# # python为了提供了获取容器对象内部属性或方法的固定用法
# # 统一采用 句点符  .
# # 句点符的左边肯定是一个容器类型(里面存了一堆名字)  # 模块
# print(User.school)
# print(User.func)

# 对象
# obj = User('jason')
# print(obj.__dict__)
# print(obj.name)
# print(obj.school)
# print(obj.func)
# 属性查找顺序   先从自身找，会去产生它的类里面去找，还会去类的父类的里面找

# 定义一个类你就把它看成是 一个新的数据类型
# l = [1,2,3,4,5,6]
# print(type(l))
# 往列表中添加值的方式
"""
append末尾追加值
insert按照指定的索引位置插值
extend
# l.append([12,22,33])  # [1, 2, 3, 4, 5, 6, [12, 22, 33]]
l.extend([12,22,33])  # [1, 2, 3, 4, 5, 6, 12, 22, 33]
"""
# class Demo:
#     pass
# obj = Demo()
# print(type(obj))

# 绑定方法
# 在类中定义的函数 叫方法  类可以直接来调用 但是需要手动传self参数
# 在没有被任何装饰器装饰的情况下 类中的方法是绑定给对象的
# 绑定:谁来调就将谁当做第一个参数自动传入

# 函数与方法区别
# 在调用函数和方法的区别在于 调用时是否会给你自动传参 如果自动传参那么就叫方法
# 如果不能自动传参 那么就叫函数


# 封装
"""
致命三问:
什么是封装？
    装:将一大堆名字装到一个容器中
    封:隐藏起来 对内公开对外隐藏
为什么要有封装？
    将复杂丑陋的接口隐藏起来，暴露给用户简单易操作的接口，还可以对这个接口的操作增加一系列限制条件
如何使用
"""
class User:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def tell_info(self):
        print('%s:%s:%s'%(self.__name,self.__age,self.__gender))


    def set_info(self,name,age,gender):
        if not isinstance(name,str):
            print('名字必须是str类型')
        if not isinstance(age,int):
            print('age must be a number')
        if not isinstance(gender,str):
            print('gender必须是str类型')
        self.__name = name
        self.__age = age
        self.__gender = gender
obj = User('jason',18,'male')
obj.tell_info()
# obj.set_info(123,'male',666)
obj.set_info('egon',19,'male')
# print(obj.__name)
# obj.__sex = 'sexy'
# print(obj.__sex)
# 封装特点:
# 1.仅仅是语法层面上的变形 会将__属性名 变形成_类名__属性名
# 2,这种封装仅仅只在类的定义阶段有效
# 3.对内开放对外隐藏













































