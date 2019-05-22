## 字符编码

重点

```python
'''
1. 什么是字符编码：将人识别的字符转换计算机能识别的01，转换的规则就是字符编码表
2. 常用的编码表：ascii、unicode、GBK、Shift_JIS、Euc-kr
3. 编码操作：编码encode()、解码decode()
'''
```

知识储备

```python
# 电脑三大核心：cpu - 内存 - 硬盘(数据的存取过程)
# 软件及python解释器读取文件过程：启动 - 读取 - 展示|解释执行
# python2环境的文件头：# coding: 编码格式
```

简介与发展

```python
'''
1. ascii - 各国编码 - 万国编码
2. 存取不一致的乱码现象
3. unicode与utf-8
'''
```

核心

```python
# 编码操作：编码encode()、解码decode()
```





## 字符与字节

重点

```python
'''
1. 字节的存储方式：8个二进制位
2. 字符所占字节数：根据编码的不同，所占字节数可能不同
3. 三种格式字符串：u''、b''、r''
'''
```

了解

```python
'''
u、b格式字符串转换: str(b'', encode='utf-8')、bytes(u'', encode='utf-8')
'''
```





## 文件操作

重点

```python
'''
1. 文件操作的三步骤：打开文件 - 使用文件 - 关闭文件
2. 文件操作三要素：文件源、操作模式、编码
3. with语法：with open(...) as 别名, ..., open(...) as 别名: pass
4. 重点方法：read() | write() | readline() | close() | f.flush() | f.seek()
'''
```

操作模式

```python
'''
主模式：r | w | a
从模式：b | t | +
了解：x | U
'''
```

操作方法

```python
'''
读：read() | readline() | readlines()
写：write() | writelines() | flush()
光标：seek() | tell()
特征：encoding | closed

了解：readable() | writable() | name 
'''
```

案例

```python
'''
1. 文件复制
2. 文件修改

了解：py文件脚本机制
'''
```



## 函数初级

### 简介

```python
# 函数是一系列代码的集合，用来完成某项特定的功能
```

### 优点

```python
'''
1. 避免代码的冗余
2. 让程序代码结构更加清晰
3. 让代码具有复用性，便于维护
'''
```

### 函数四部分

```python
'''
1. 函数名：使用该函数的依据
2. 函数体：完成功能的代码块
3. 返回值：功能完成的反馈结果
4. 参数：完成功能需要的条件信息
'''
```

### 函数的定义与调用的完整语法

```python
# 1、定义
# def 是声明函数的关键字，后面跟着函数名，括号内是函数的参数
def 函数名(参数1,参数2,参数3,...): 
    '''注释'''
    函数体  # 函数体写具体的逻辑代码
    return 返回的值 # retrun后面是函数的返回值，是函数体代码的运行成果

# 2、调用
函数名(参数1,参数2,参数3,...)

'''注：
	-- 先定义再调用
	-- 函数名存放的是函数地址
	-- ()会触发函数体的执行
	-- 函数执行完毕得到的是函数的返回结果，通常称之为函数的返回值，也称函数值
'''
```





## 函数详解

### 根据函数体划分

- 空函数：用来罗列功能

```python
# 空函数指的是函数体用pass占位，pass代表什么也不做
def func():           
    pass 

# func()：调用后什么是都不干
```

- 非空函数：正常可以完成某项功能

```python
def func():           
    print('非空函数') 
    
# func()：调用后执行函数体
```



### 根据参数列表划分

- 无参函数：不需外界资源

```python
def start():
    print('系统启动')
```

- 有参函数：需要外键资源

```python
def login(usr, pwd):
    if usr == 'owen' and pwd == '123':
        print('登录通过')
	else:
        print('登录失败')
```



### 根据返回值划分：return是用来结束函数的

- 空返回：返回None

```python
def demo(x, y):
    print( x + y )
    
def demo(x, y):
    print( x + y )
    return
```

- 一值返回

```python
def demo(x, y):
    return x + y
```

- 多值返回

```python
def demo(x, y):
    return x + y, x - y, x * y, x / y
```

