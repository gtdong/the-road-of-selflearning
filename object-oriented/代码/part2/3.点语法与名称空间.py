
def fn():
    pass

class Fn():
    def a_fn():
        pass
    pass

import md

print(fn, fn.__dict__)
print('========================================')
print(Fn, Fn.__dict__)
print('========================================')
print(md, md.__dict__)
print('========================================')

# 访问名字的底层
print(Fn.__dict__['__module__'])
# 访问名字的语法优化
print(Fn.__module__)
# 总结：对象.名字 本质 对象.__dict__['名字']


# 赋值
fn.name = '我写的函数'
print(fn.__dict__)
print(fn.__dict__['name'])
print(fn.name)


# 了解：对象的名称空间，与对象内部的名称空间不是同一个
print('========================================')
def func():
    a = 10
    b = 20
    # print(func.__dict__)
    print(locals())
func()
print(func.__dict__)

# 记住：
# 对象.名字 = 值 是为该对象添加一个名称空间的名字，
# 也只能通过 对象.名字 来使用
func.name = 'func function'
print(func.name)

