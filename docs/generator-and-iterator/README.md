## 复习

```python
'''
1.函数的参数：实参与形参
	形参：定义函数()中出现的参数
	实参：调用函数()中出现的参数
	形参拿到实参的值，如果整体赋值(自己改变存放值的地址)，实参不会改变，(可变类型)如果修改内部内容，实参会跟着变化
	
	位置实参 - 只能对位置形参赋值
	关键字实参 - 可以对所有(不包含可变长位置形参)形参赋值
	
	位置形参 - 必须出现在最前，且必须传值
	默认形参 - 出现在位置形参后*前，可以不用传参
	可变长位置形参 - 接收所有位置形参、默认形参没有接收完的位置实参
	有无默认值关键字形参 - 必须出现在所有位置形参之后，有默认值可以不用传参，没有默认值必须通过关键字实参传值
	可变长关键字形参 - 接收所有有名字的关键字形参没有接收完的关键字实参
	
def fn(a, b=10, *args, c, d=20, e, **kwargs): pass

	
2.函数的嵌套调用
	在一个函数的内部调用另一个函数：在函数内部遇到调用其他函数，就进入其他函数内部，全部走完 回到调用其他函数 的入口

3.函数对象
	- 直接赋值、可以加()调用、作为其他函数的参、作为函数的返回值、作为容器对象的元素(成员)
4.名称空间与作用域
	- LEGB：查找顺序LEGB | 加载顺序BGEL
	
5.函数的嵌套定义 - 闭包
	- 函数的嵌套定义：在一个函数内部定义另一个函数，内部的函数就是闭包
	- 应用场景：
		- 延迟执行
		- 装饰器

6.装饰器
'''


```

## 带参装饰器

```python
# 为什么要出现带参装饰器
def outer(func):
    # outer与inner之间要使用外部数据
    # 可以解决的方案路径，给outer添加参数，但是outer的参数是固定一个，就是被装饰的函数
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return inner

# 所以只能使用函数的闭包，通过外层函数给内存函数传递参数的方式
def wrap(*arg, **kwargs):
    def outer(func):
        # 就可以使用wrap中的*arg, **kwargs，就是要使用的外部数据
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return inner
    return outer

a = 10
b = 20
@wrap(a, b)  # @wrap(10, 20) => @outer => fn = outer(fn) => fn = inner
def fn():
    pass

```

## wraps修改函数文档注释

```python
# 为什么要出现该语法

from functools import wraps
def outer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return inner
def fn():
    '''
    fn的文档注释
    '''
   
print(fn.__doc__)  # fn本质是inner，使用打印fn.__doc__本质是inner函数的文档注释

# 形参假象：让打印fn.__doc__显示的效果是fn自己的
```



## 今日内容

```python
'''
基础残留：三元表达式，列表字典推导式

迭代器：可迭代对象、迭代器对象、for循环迭代器、枚举对象、生成器(自定义的迭代器)

内置函数：匿名函数、常用的内置函数

模块：模块，包，常用模块
'''
```



## 三元表达式

```python
# what：就是简写if...else...结构，且都只有一条语句
# 语法：结果1 if 条件 else 结果2
# 注意：结果1|2不一定要与条件有必然关系，条件只是选择结果1或结果2的判断依据

# 案例：获得两个数中的大值 | 小者
n1 = int(input('n1: '))
n2 = int(input('n2: '))
res = n1 if n1 > n2 else n2
print(res)
res = n2 if n1 > n2 else n1
print(res)
```



## 列表与字典的推导式

```python
# 列表推导式
# 语法：[结果 for 结果 in 可for循环操作的对象]
# 案例：[v for v in 'abc'] => ['a', 'b', 'c']
# 案例：['奇数' if i % 2 != 0 else '偶数' for i in range(1, 11)]


# 字典推导式
# 语法：{k: v for k, v in 可for循环操作的对象(每一次循环的结果可以被解压为两个值)}

# 案例: [('a', 1), ('b', 2)] => {'a': 1, 'b': 2}
# dic = {k: v for k, v in [('a', 1), ('b', 2)]}

# 案例：{i: 0 for i in 'abc'} == {}.fromkeys('abc', 0) == {'a': 0, 'b': 0, 'c': 0}

```





## 迭代器

#### 可迭代对象

```python
# 有__iter__()方法的对象都称之为 可迭代对象

# 可迭代对象：可以被转化为不依赖索引取值的容器，这样的对象就叫做可迭代对象
#       -- 对象.__iter__() 来生成不依赖索引取值的容器
#       -- 结论：有__iter__()方法的对象都称之为 可迭代对象

# 可迭代对象.__iter__() => 和该对象有关系的迭代器对象 dict_keyiterator object
box = dic.__iter__()  

# 可迭代对象有哪些：str | list | tuple | set | dict | range() | enumerate() | file | 生成器对象
```



#### 迭代器对象

```python
# 有__next__()且可以通过__next__()进行取值的容器

# 迭代器对象：可以通过__next__()的方式进行取值的容器，且取一个少一个
#       -- 结论：有__next__()且可以通过__next__()进行取值的容器
#       -- 注意：迭代器对象自身也拥有__iter__(), 通过该方法返回的是迭代器对象自身

res = box.__next__()  # 从迭代器对象(容器)取出值，取一个少一个
box = box.__iter__()  # 迭代器对象.__iter__()得到迭代器对象本身

# 迭代器对象有哪些：enumerate() | file | 生成器对象
```



#### for迭代器

```python
# 可以操作迭代器对象及可迭代对象，且能自动处理异常的循环，内部同迭代器对象__next__()来取值

# 迭代器(for循环)：就是用来从可迭代对象中进行取值的循环方法 | 语法：for 变量 in 对象:
#       -- 1.通过对象.__iter__()获取其对应的迭代器对象
#           -- for可以操作迭代器对象及可迭代对象，统一写法，所以迭代器和可迭代对象都有__iter__()
#       -- 2.在内部通过迭代器对象的__next__()进行取值，将值赋值给 语法中的变量，取一个少一个
#       -- 3.当迭代器对象取完了，在内部自动捕获异常，并结束循环取值
ls = [1, 2, 3, 4, 5]
for v in ls:
    print(v)
for v in ls.__iter__():
    print(v)
```



#### 生成器

```python
# 自定义的迭代器对象，写法和函数非常相似，但是内部用yield来对外部返回值，且可以有多个yield
# 语法：
def my_generator():  # => [1, 2, 3]
    yield 1
    yield 2
    yield 3
# 生成器名() 不是函数的调用，而是得到生成器对象，生成器对象就是迭代器对象，所有有__next__()方法
obj = my_generator()

# 一个个取值
# 去生成器中执行代码，拿到遇到的第一个yield后面的值，并停止运行
print(obj.__next__())
# 再接着上一个yield，再进行往下执行代码，再拿到下一个个yield后面的值，并停止运行
print(obj.__next__())
# 重复上面的过程，如果没有遇到yield，就报错
print(obj.__next__())

# 循环取值
while True:
    try:
        print(obj.__next__())
    except Exception:
        break
        
        
# 案例：
# 将传入的值扩大两倍返回
def fn1(*args):
    i = 0
    while i < len(args):
        yield args[i] * 2
        i += 1

for v in fn1(10, 20, 30, 40, 50):
    print(v)
    

# 依次获取阶乘 1! 2! 3! ...
def fn2():
    total = 1
    count = 1
    while True:
        total *= count
        yield total
        count += 1
obj = fn2()
print(obj.__next__())  # 1！
print(obj.__next__())  # 2！
print(obj.__next__())  # 3！
# ...
# print(obj.__next__())  # n!

```

#### 了了解：生成器的send

```python
# send：
# 1.send会为当前停止的yield传入参数，内部可以通过yield来接收传入的参数
# 2.send自身也会调用__next__()去获取下一个yield的结果

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
```



#### 枚举对象

```python
# 枚举对象：为迭代器对象产生迭代索引

ls = [3, 1, 2, 5, 4]
list(enumerate(ls))  # => [(0, 3), (1, 1), (2, 2), (3, 5), (4, 4)]

dic = {'a': 100, 'b': 200}
print(list(enumerate(dic)))  # => [(0, 'a'), (1, 'b')]
```





## 递归

```python
# 递归：函数直接或间接调用自己
# 回溯：找寻答案的过程
# 递推：通过最终的值反向一步步推出最初需要的结果

# 前提：
# 1.递归条件是有规律的
# 2.递归必须有出口


# 拿递归求得年纪
def get_age(num):
    if num == 1:
        return 58
    age = get_age(num - 1) - 2
    return age
age = get_age(10)
print(age)


# 传入一个num，求得该num的阶乘
# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4!
# 4! = 4 * 3 * 2 * 1 = 4 * 3!
# 3! = 3 * 2 * 1 = 3 * 2!
# 2! = 2 * 1 = 2 * 1!
# 1! = 1
def get_total(num):
    if num == 1 or num == 0:
        return 1
    total = num * get_total(num - 1)  # 3 * 2! => 2 * 1!1 => 1 => 2 * 1
    return total
print(get_total(3))
```



## 内置函数

#### 匿名函数

```python
# 匿名函数: 没有名字的函数

# 特点：
# 1.用lambda声明匿名函数
# 2.没有函数名，lambda与:之间一定是参数列表，参数列表省略()，且支持所有参数语法
# 3.匿名函数没有函数体，只有返回值，所有省略了return，且返回值只能有一个
#       -- (不能将多个返回值自动格式化为元组)

# lambda 参数1, ..., 参数n: 一个返回值


# 应用场景：
# 1.用一个变量接收，该变量就充当与函数的名字 - 不常见
# func = lambda x, y: (x + y, x - y)
# print(func(10, 20))

# 2.结合内置函数来使用
max([1, 2, 6, 5, 3], key=lambda x: x)
dic = {
    'Bob': (1, 88888),
    'Ben': (2, 300000),
    'Tom': (3, 99999)
}
min(dic, key=lambda k: dic[k][1])  # 按薪资求最小值


```

#### 内置函数

```python
# max函数的工作原理
# 1.max要去遍历所有求大值的数据，这些一一被遍历出来的数要被依次传入key=fn的fn中
#       -- fn必须有参数，且只有一个参数，就是当前被遍历出来的被比较的数据
# 2.max再根据fn的返回值决定比较大小的依据

dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}
def fn2(k):
    # return k  # 求名字最大
    # return dic[k][0]  # 求工号最大
    return dic[k][1]  # 求薪资最大
max_p = max(dic, key=fn2)
print(max_p)
```



```python
# min函数的工作原理
# 1.min要去遍历所有求小值的数据，这些一一被遍历出来的数要被依次传入key=fn的fn中
#       -- fn必须有参数，且只有一个参数，就是当前被遍历出来的被比较的数据
# 2.min再根据fn的返回值决定比较大小的依据

dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}
res = min(dic, key=lambda x: dic[x][1])
print(res)
```



```python
# 排序：sorted
dic = {
    'owen': (1, 88888),
    'egon': (2, 300000),
    'liuXX': (3, 99999)
}

# 总结：排序的可迭代对象，排序的规则，是否反转
res = sorted(dic, key=lambda k: dic[k][1], reverse=True)  # 按薪资排序的人名list
for k in res:
    print(k, dic[k][1])
```



```python
# map：映射 - 格式化每一次的遍历结果
names = ['Owen', 'Egon', 'Liuxx']
def fn(x):
    # print(x)
    # 将所有名字全小写
    return x.lower()

res = map(fn, names)
print(list(res))
```



```python
# 合并：reduce
from functools import reduce
# 求[1, 3, 4, 2, 10]所有元素的总和
res = reduce(lambda x, y: x + y, [1, 3, 4, 2, 10])
print(res)
```



```python
# 已见过的
# 1.类型转换：int() tuple()
# 2.常规使用：print() input() len() next() iter() open() range() enumerate() id()
# 3.进制转换：bin() oct() hex() 将10进制转换为2 | 8 | 16进制
print(bin(10))  # 0b1010
print(oct(10))  # 0o12
print(hex(10))  # 0xa

# 3.运算：abs()
print(abs(-1))  # 绝对值
print(chr(9326))  # 将ASCII转换为字符
print(ord('①'))  # 逆运算
print(pow(2, 3))  # 2的3次方
print(pow(2, 3, 3))  # 2的3次方对3求余
print(sum([1, 2, 3]))  # 求和

# 4.反射：getattr() delattr() hasattr() setattr()

# 5.面向对象的相关方法：super() staticmethod() classmethod()
def fn():pass
print(callable(fn))  # 对象能不能被调用

# 6.原义字符串
print('a\nb')
s = ascii('a\nb')
print(s)
s = repr('a\nb')
print(s)
print(r'a\nb')

print(all([1, 0, 0]))
print(any([0, 0, 1]))

# compile() exec() eval()
```







