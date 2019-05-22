a = 10
print(a)

# 功能的复用
def print_num(a):
    print(a)
print(10)
print(20)

# 文件的复用
from md import print_num as pn
pn(100)
pn(200)

# 解决：函数集合体的复用
# 不管是单独封装函数或是将函数封装到文件中，直接导入函数名，每个函数使用还是个体
def fn1():
    print('fn1 run')
def fn2():
    print('fn2 run')
def fn3():
    print('fn3 run')

fn1()
fn2()
fn3()


from md import fn1 as f1, fn2 as f2, fn3 as f3
f1()
f2()
f3()

# 如何做到函数集合体的复用，也就是拿到函数的集合体对象，该对象就包含了所有的函数功能
import md
md.fn1()
md.fn2()
md.fn3()

print('=============================')
# 引子：模块可以单独使用功能，也能通过模块综合管理所有的功能，
# 那在一个文件中，单独使用就是定义函数，那如何综合管理多个功能

class FnBox:  # FnBox就是自定义的类，fn1、fn2、fn3就是类中的行为(功能) => 如何在类中定义特征(属性)
    def fn1():
        print('fn1 run')
    def fn2():
        print('fn2 run')
    def fn3():
        print('fn3 run')
FnBox.fn1()
FnBox.fn2()
FnBox.fn3()

