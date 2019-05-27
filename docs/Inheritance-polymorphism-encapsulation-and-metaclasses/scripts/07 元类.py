# class Demo:
#     def func(self):
#         pass


# obj = Demo()
# print(type(obj))  # obj = Demo()
# print(type(Demo))  # Demo = type()

# 所有你写的类默认情况下都是type产生的
# 产生类的类称之为       元类！！！  即type就是元类

# 类三大特征
"""
1.类名
2.父类
3.类的名称空间
"""

# eval 与 exec
# res = """
# for i in range(5):
#     print(i)
# """
# eval(res)
# exec(res)
# eval与exec都可以识别字符串中代码并执行，但是eval不支持逻辑性代码

#
# class_name = 'User'
# class_bases = (object,)
# res = """
# school ='oldboy'
# def __init__(self,name):
#     self.name = name
# def func(self):
#     pass
# """
# class_attrs = {}
# exec(res,{},class_attrs)
# User = type(class_name,class_bases,class_attrs)
# print(User)
# print(User.school)
# obj = User('jason')
# print(obj.name)
# print(obj)


# class MymetaClass(type):
#     def __call__(self, *args, **kwargs):
#         # 1.先创建一个对象的名称空间  __new__
#         # 2.往改名称空间中丢一堆名字  __init__
#         # 3.产生好的对象返回出去
#         # 1.产生一个空对象
#         obj = self.__new__(self)
#         # 2.实例化该对象
#         self.__init__(obj, *args, **kwargs)
#         # 3.返回该对象
#         return obj
#         # return super().__call__(*args,**kwargs)
# class Demo(metaclass=MymetaClass):  # 指定Demo的元类是MymetaClass
#     pass
# obj = Demo()
# print(obj)
# print(type(obj))

"""
<__main__.Demo object at 0x0000022048F083C8>
<class '__main__.Demo'>


<__main__.Demo object at 0x00000170FB1D82B0>
<class '__main__.Demo'>
"""




# 表名  主键  一对字段
class MemetaClass(type):
    def __new__(cls, class_name,class_bases,class_attrs):
        if class_name == 'Userinfo':
            raise TypeError('我不想鸟你')
        if 'school' in class_attrs:
            class_attrs['school'] = '澳门最大线上赌场开业啦'
        class_attrs['table_name'] = 'userinfo'
        class_attrs['primary_key'] = 'id'
        return type.__new__(cls,class_name,class_bases,class_attrs)
class User(object,metaclass=MemetaClass):
    school = 'oldboy'
print(User.__dict__)


