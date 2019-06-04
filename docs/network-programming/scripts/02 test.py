# res = (1,)
# l = [1,]
# print(type(res))
#
# # 类无论传多少关键字参数都能够实例化
# d = dict(name='jason',password='123')
# print(d)
#
#
# class MyClass(dict):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#
#     def __getattr__(self, item):
#         return self.get(item)
#
#     def __setattr__(self, key, value):
#         self[key] = value
# obj = MyClass(name='jason')
# obj1 = MyClass(path='sahjkdaskjd')
# # print(obj.name)
# # print(obj1.path)
# obj.xxx = '123'
# print(obj)
# print(obj.xxx)

class Demo(object):
    def __call__(self, *args, **kwargs):
        print('hello')
obj = Demo()
obj()