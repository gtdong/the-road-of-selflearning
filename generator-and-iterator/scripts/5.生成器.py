# 生成器：自定义的迭代器对象
def fn():
    print(1)
    yield 666
    print(2)
    yield 888
    print(3)
# print(fn())
"""
obj = fn()  # generator object => [666, 888]
print(obj)
# 去生成器中执行代码，拿到遇到的第一个yield后面的值，并停止运行
print(obj.__next__())
# 再接着上一个yield，再进行往下执行代码，再拿到下一个个yield后面的值，并停止运行
print(obj.__next__())
# 重复上面的过程，如果没有遇到yield，就报错
print(obj.__next__())
"""
for v in [666, 888]:
    print(v)

print('--------------------')
# 将传入的值扩大两倍返回
# def fn1(a, b, c):
#     yield a * 2
#     yield b * 2
#     yield c * 2
#
# for v in fn1(10, 20, 30):
#     print(v)

# 解决方案
# def fn1(*args):
#     i = 0
#     while i < len(args):
#         yield args[i] * 2
#         i += 1
#
# for v in fn1(10, 20, 30, 40, 50):
#     print(v)


# 依次获取阶乘 1! 2! 3! ...
def fn2():
    total = 1
    count = 1
    while True:
        total *= count
        yield total
        count += 1

obj = fn2()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())


print('=================')
# 了了解
# def fn3():
#     msg = yield 1
#     print(msg)
#     yield 2
# obj3 = fn3()
# print(obj3.__next__())
# # 1.send会为当前停止的yield传入参数，内部可以通过yield来接收传入的参数
# # 2.send自身也会调用__next__()去获取下一个yield的结果
# result = obj3.send('ooo')
# print(result)



def fn4(peoples):
    count = 0
    print('%s在面试' % peoples[count])
    while count < len(peoples):
        name = yield peoples[count]
        count += 1
        print(name + "叫来%s来面试" % peoples[count])

peoples = ['张三', '李四', '王五']
obj4 = fn4(peoples)
name = obj4.send(None)  # 第一次没有yield接收值，所以只能调__next__()，或是send(None)
print(name + '面试完毕')
while True:
    try:
        name = obj4.send(name)
        print(name + '面试完毕')
    except Exception:
        print('所有人面试完毕')
        break




