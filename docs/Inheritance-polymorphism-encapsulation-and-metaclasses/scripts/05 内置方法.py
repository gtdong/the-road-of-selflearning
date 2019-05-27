class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password

    def __str__(self):
        # return '%s:%s'%(self.name,self.password)
        return '我被打印了，自动触发'

    def __getattr__(self, item):
        print(item)

    def __setattr__(self, key, value):
        print(key,value)
"""
ORM
类映射成数据库的一张表
对象映射成表中的一条记录
对象获取属性映射成获取记录的某个字段对应的值
"""
# __str__对象被执行了打印操作  自动触发
# obj = User('jason',123)
# print(User)
# print(obj)

# __getattr__ 当对象获取一个不存在的属性时候才会触发
# obj = User('jason',18)
# print(obj.name)


# __setattr__: obj.name = 'xxx'  固定句式
# obj = User('jason',18)
# obj.sex = 'sexy'

# class Demo(dict):
#     def __getattr__(self, item):
#         return self.get(item)
# d = Demo(name='jason',password=123)
# print(d.name)
# print(d.password)


















