# BMI指数
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
# class User:
#     def __init__(self,height,weight):
#         self.height = height
#         self.weight = weight
#     @property
#     def bmi(self):
#         return self.weight/(self.height**2)
# # user = User(1.83,75)
# # user.bmi()
# user = User(1.65,85)
# print(user.bmi)


# class User:
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,val):
#         if not isinstance(val,str):
#             print('name字段必须是str类型')
#         self.__name = val
#
#     @name.deleter
#     def name(self):
#         print('不能删啊 老弟！')
#
# obj = User('jsaon',18)
# print(obj.name)
# obj.name = 'egon'
# print(obj.name)
# del obj.name
# class User:
#     def __init__(self,name):
#         self.name = name
#
#     def func(self):
#         print('func')
#
#     @classmethod
#     def foo(cls):
#         print(cls)
#
#     @staticmethod
#     def bar(x,y):
#         print('bar')
# obj = User('jason')
# obj.func()
# User.foo()
# obj = User('jason')
# User.bar(1,2)
# obj.bar(1,2)
























