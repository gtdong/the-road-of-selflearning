
## 一、如何定义函数

```python
'''
1、功能的单一化
2、函数内部需要外部的资源：通过函数的参数来实现
3、函数执行后的结果需要告诉外界：通过返回值告诉给外界
'''
```



## 二、函数的参数

#### 形参与实参

```python
'''
形参：在函数定义时()里出现的参数
	-- 形参本身没有实际值(意义)，在函数调用时，传入什么实参，形参就装有什么值
实参：在函数调用时()里出现的参数
	-- 实参有实际值(意义)
	
重点：函数调用传参：将实参的值赋值给形参 | 形参要获取外界的值只能通过实参进行获取
'''

def fn(a, b):  # a, b:形参
    pass

a = 10
fn(a, 20)  # a, 20：实参

```

#### 两种实参

```python
'''
位置实参：
1.传参两种方式：实参名 | 实参具体值
2.必须按位置对形参进行传值


关键字实参：
1.传参两种方式：形参名=实参名 | 形参名=实参值
2.可以指名道姓对形参进行传值，所以可以不用按位置进行传参
'''

def func(a, b, c):
    print(a, b, c)

# func(10, b=20, 200)  报错：SyntaxError: positional argument follows keyword argument
# 重点：两种实参在一起进行传参时：必须位置在前，关键字在后
```



#### 两大形参分类

```python
'''
形参种类：
1）位置形参
    -- 普通位置形参
    -- 默认值形参
    -- 可变长位置形参

2）关键字形参
    -- 有默认值关键字形参
    -- 无默认值关键字形参
    -- 可变长关键字形参
'''
def fn(a, b, *, x, y):  # 位置形参:a, b  关键字形参: x, y
    pass

'''
重点：
1.*为分水岭
2.位置实参只能给位置形参进行传值
3.关键字实参可以给位置形参与关键字形参进行传值
'''
```



#### 两个带默认值的形参

```python
def fn2(a=10, *, x=20):
    print(a, x)
fn2(100, x=200)
# 总结：
# 1.有默认值的参数可以不用传值
# 2.*前有默认值的叫默认值参数，属于位置形参，可以被位置及关键字实参进行传值
# 3.*后有默认值的叫有默认值的关键字形参，属于关键字形参，只能被关键字实参进行传值
# 4.如果省略*, 有默认值的形参都是默认值参数

```



#### 不带默认值与带默认值形参结合使用

```python
def fn3(a, b=10, *, x, y=20, z):
    print(a, b, x, y, z)
fn3(100, x=200, z=300)
# 总结：
# 1.没有默认值的必须传参，有默认值的可以传也可以不传
# 2.位置有值的必须出现在无值之后，关键字顺序不做要求
```



#### 可变长位置形参与可变长关键字形参

```python
def fn4(a, b=10, *args, x, **kwargs):
    print(a, b, x)
    print(args)
    print(kwargs)
fn4(10, 20, 30, x=100, y=200, z=300)
# 总结：
# 1.可变长是用来接收未接收完的值(接收0到n个)：
#   -- *args用来接收所有没有接收完的位置(只能接收位置实参)
#   -- **kwargs用来接收所有没有接收完的关键字(只能接收关键字实参)
# 2.*args必须出现在所以位置参数之后，**kwargs必须出现在所以参数之后


# 常见应用场景
# 假设第一个位置永远是参数name
def func4(*args, **kwargs):
    name = args[0]  # 将name抽出来

def func44(name, *args, **kwargs):
    # name 可以直接接收，省了抽出来的过程
    pass
```



#### 总结

```python
'''
1.位置实参只能给位置形参传值
2.关键字实参可以给位置及关键字形参传值
3.有默认值的可以不用传参
4.可变长位置形参只能接受位置实参，接受位置形参没有接收完的位置实参，存放到元组中
5.可变长关键字形参只能接受关键字实参，接受关键字形参没有接收完的关键字实参，存放到字典中
6.*args必须出现在所有位置形参之后，**kwargs必须在所有形参之后
'''
```



#### 可变长整体传参：打散传值

```python
def fn(*args, **kwargs):
    print(args, kwargs)
    
fn([1, 2, 3], {'a':1 , 'b': 2})  # =>接收到的 ([1, 2, 3], {'a':1 , 'b': 2})  {}
fn(*[1, 2, 3], **{'a':1 , 'b': 2})  # =>接收到的 (1, 2, 3)  {'a':1 , 'b': 2}

# 注：字符串也可以作为单列集合进行打散传递
fn(*'abc')  # => ('a', 'b', 'c')  {}
```



## 三、函数对象

```python
# 函数名就是存放了函数的内存地址，存放了内存地址的变量都是对象，即 函数名 就是 函数对象

# 函数对象的应用场景
# 1 可以直接被引用
# 2 可以当作函数参数传递
# 3 可以作为函数的返回值
# 4 可以作为容器类型的元素

# 功能体
def add(n1, n2):
    return n1 + n2

def low(n1, n2):
    return n1 - n2

def jump(n1, n2):
    return n1 * n2

# 完成功能
def computed(n1, n2, fn):  # fn = add|low|jump
    res = fn(n1, n2)  # 调用具体的功能
    return res

# 功能对应关系
method_map = {  # 指令与函数对象的对应关系
    '1': add,
    '2': low,
    '3': jump
}

# 获取功能
def get_method(cmd):
    if cmd in method_map:
        return method_map[cmd]  # 返回 add|low|jump
    return add  # 当指令错误，add作为默认功能

while True:
    cmd = input('cmd: ')
    res = get_method(cmd)(10, 20)  # 根据指令获取功能并调用得到结果
    print(res)
```



## 四、函数的嵌套调用

```python
# 函数的嵌套调用：在一个函数内部调用另一个函数
# 求两个数最大值
def max_two(n1, n2):
    if n1 > n2:
        return n1
    return n2

# 求三个数最大值
def max_three(n1, n2, n3):
    max = max_two(n1, n2)
    return max_two(max, n3)

# 求四个数最大值
def max_four(n1, n2, n3, n4):
    max = max_three(n1, n2, n3)
    return max_two(max, n4)
print(max_four(20, 50, 30, 50))
```





## 五、名称空间

```python
# 名称空间：存放名字与内存空间地址对应关系的容器
# 作用：解决由于名字有限，导致名字重复发送冲突的问题 - 内置全局局部可以同时使用一个名字存放不同地址

# 三种名称空间
# Built-in：内置名称空间；系统级，一个；随解释器执行而产生，解释器停止而销毁
# Global：全局名称空间；文件级，多个；随所属文件加载而产生，文件运行完毕而销毁
# Local：局部名称空间；函数级，多个；随所属函数执行而产生，函数执行完毕而销毁

# 加载顺序：Built-in > Global > Local
# 	-- 采用堆栈存储数据的方式(压栈)，导致内置最后被访问
```



## 六、函数的嵌套定义

```python
# 函数的嵌套定义：在函数内部定义函数
# 诞生的理由：一个函数想使用另一个函数内部的变量，可以定义在其内部
def func():
    a = 10
    def fn():
        print(a)
    return fn

new_fn = func()
new_fn()
```



#### 两个与函数有关的关键字：global nonlocal

```python
# global：统一局部与全局的变量名
num = 10
def outer():
    # global num
    # num = 100
    def inner():
        global num
        num = 1000
        
# nonlcal: 统一局部与嵌套局部的变量名
def outer():
    num = 100
    def inner():
        nonlocal num
        num = 1000
```



## 七、作用域

```python
# 作用域：名字起作用的范围
# 作用：解决同名字可以共存问题 - 不同作用域相同名字的值都能在其作用域范围下进行使用
'''
四种作用域: LEGB
Built-in：内置作用域 - 所有文件所有地方都可以被访问
Global：全局作用域 - 在当前文件的所有位置
Enclosing：嵌套作用域 - 自身内部与内部的子函数
Local：局部作用域 - 只有自身内部
'''
# 加载顺序：Built-in > Global > Enclosing > Local
# 访问(查找)顺序：报错 < Built-in < Global < Enclosing < Local
# 作用范围：Built-in > Global > Enclosing > Local
```



## 八、闭包

```python
# 闭包：定义在函数内部的函数，这个内部的函数就是闭包

# 应用场景：
# 1.可以去使用其他函数的内部变量，且还可以保证调用位置不变(闭包的函数对象作为那个函数的返回值)
def outer():
    count = 3000
    def fn():
        print(count)  # 能使用outer内部的变量count
    return fn
# 还是在外界调用
outer()()  # outer()() => fn() => 调用fn


# 2.延迟执行（外层函数可以为内存函数传递参数）
import requests
def outer(url):
    def show_html():
        response = requests.get(url)
        print(response.text)
    return show_html

# 制作 爬百度与新浪的 函数对象
show_baidu = outer('https://www.baidu.com')
show_sina = outer('https://www.sina.com.cn')

# 延迟到需求来了，需要爬百度，就用百度函数对象，需要爬新浪，就用新浪函数对象
show_baidu()
show_sina()
show_baidu()
```



## 九、装饰器

```python
# 装饰器：装饰器就是闭包的一个应用场景
#       -- 外层函数与内存函数形成的闭包结构的一种综合使用

# 重点：开放封闭原则
# 开放：拓展功能的点是开放的 - 可以为之前的函数添加新功能
# 封闭：1.不能改变原函数的源代码  2.还有通过原函数的函数对象来调用函数

def huaping():
    print('插花功能')

temp = huaping
def my_huaping():
    temp()
    print('观赏功能')
huaping = my_huaping

huaping()

# ----------------------------------------

def huaping():
    print('插花功能')

def outer(temp):  # temp = huaping
    def my_huaping():
        temp()
        print('观赏功能')
    return my_huaping
huaping = outer(huaping)  # huaping = my_huaping

huaping()


# ----------------------------------------------
def outer(temp):  # temp = huaping
    def my_huaping():
        temp()
        print('观赏功能')
    return my_huaping

@outer  # huaping = outer(huaping)
def huaping():
    print('插花功能')
    
huaping()


# ------------------------------------------
# 被装饰的函数可能有参有返：装饰器模板，可以满足所有参数，且能装饰原函数返回值
def outer(func):  # temp = huaping
    def inner(*args, **kwargs):
        pass
        res = func(*args, **kwargs)
       	pass
    	return res
    return inner

@outer
def any_method():
    pass

```

#### 装饰器案例

```python
# 为登录功能添加账号检验功能：必须是3个及以上英文字母组成
def check_user(func):
    def inner(user, pwd):
        if not (user.isalpha() and len(user) >= 3):
            return '账号不合法'
        res = func(user, pwd)
        return res
    return inner

# 为登录功能添加密码检验功能：必须是3个及以上英文字母或数字组成
def check_pwd(func):
    def inner(*args, **kwargs):
        pwd = args[1]
        if not (pwd.isalnum() and len(pwd) >= 3):
            return '密码不合法'
        res = func(*args, **kwargs)
        return res
    return inner

# 对登录结果的修饰装饰器：True=>登录成功 False=>登录失败
def change_res(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if res == True:
            return '登录成功'
        return '登录失败'
    return inner


# 装饰器被执行的过程是从上至下
@check_user  # login = check_user(func=login) = inner
@check_pwd
@change_res
def login(user, pwd):  # 被装饰的函数对象
    if user == 'owen' and pwd == '123':
        return True
    return False

user = input('user: ')
pwd = input('pwd: ')
res = login(user, pwd)

print(res)
```
