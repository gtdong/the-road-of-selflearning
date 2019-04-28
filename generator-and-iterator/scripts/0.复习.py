# def fn1(a, b, c):
#     print(a, b, c)
#     a = 20
#     b = 200
#     c.append(888)
#     # c = [666, 888]
#     print(a, b, c)
#
# a = b = 10
# c = [666]
# fn1(a, b, c)
# print(a, b, c)

def a():
    b()
def b():
    pass
a()

def c():
    pass
def d():
    c()
d()

def x():
    print(111)  # 1
    y()
    print(222)  # 5

def y():
    print(000)  # 2
    z()
    print(000)  # 4

def z():
    print(666)  # 3
x()  # 总入口


a = 10
def aaa():pass
bbb = aaa
dic = {'fn': aaa}

def ccc(fn):
    fn()
    return ccc
ccc(aaa)

# 函数对象：包含函数所有内容的变量，该变量存放的是函数的地址
# 函数对象()：就是执行该函数的函数体，返回函数的执行结果

ccc(aaa)(bbb)

len('123')
len = 10
del len

def outer():
    x = 10
    def inner():
        print(x)
    return inner
inner = outer()
inner()


# def inner(arg):
#     print(arg)
# inner('abc')

def outer(arg):
    def inner():
        print(arg)
    return inner

print_abc = outer('abc')
print_def = outer('def')
print_abc()



def xxx(fn):  # 接收到的是原函数体
    def yyy(*args, **kwargs):
        print('...')  # 新增功能
        res = fn(*args, **kwargs)  # 调用原功能
        print('...')  # 新增功能

    return yyy

@xxx  # func = xxx(func)  # 被装饰后的函数体 = yyy， 传入的是原函数体
def func(a, b, *, x, y):  # 原函数体
    pass

func(10, 20, x=30, y=40)  # 被装饰后的函数体