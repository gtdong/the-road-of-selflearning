"""
def fn():
    a = 10
    b = 20
    print('fn run')

# 定义类，类所属文件被加载，类的内部就会被执行，
# 内部的所有名字就会产生存放到类的名称空间中
class People:
    x = 10
    y = 20
    def fn(self):
        print('fn run')
    def __init__(self):
        print('__init__ run')

    print('People run')

print(fn.__dict__)
print(People.__dict__)
"""

# 类的声明语法
class People:
    # 特征：属性
    name = '人'

    # 行为：方法
    def eat(self):
        print('在吃饭')

# 对象：类如何实例化出具体的对象: 类名()
p1 = People()
p2 = People()
# 结论1：类与每一个对象的名称空间都是独立的
print(p1.__dict__)
print(p2.__dict__)
print(People.__dict__)
# 结论2：类与每一个对象都可以使用类中的名字
print(People.name)  # 人
print(p1.name)  # 人
print(p2.name)  # 人
# 结论3：对象访问名字，优先访问自己的，自己没有再访问类的
p1.name = '张三'
p2.user = '李四'
print(People.name)  # 人
print(p1.__dict__)
print(p2.__dict__)
print(p1.name)  # 张三
print(p2.user)  # 李四
print(p2.name)  # 人
