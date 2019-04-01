



## 数字类型

```python
'''
1. 整型
a1 = 10
a2 = int(20)

2. 长整型(py2特有，py3废弃)
b1 = 12345678901234567890
b2 = long(100)

3. 浮点型
c1 = 3.14
c2 = float(5.12)

4. 复数类型
d = 2 + 3j
'''

'''
总结：
1. 只可以存放一个值：num = 1000
2. 为不可变类：num += 1
'''
```



## 字符串类型

```python
''' *****
1. 单行字符串
s1 = 'abc'
ss1 = "xyz"

2. 多行字符串
s2 = """first line
second line
last line"""

3. 字符串嵌套
i) 单、双、三引号直接可以相互嵌套
ii) 同类型引号直接嵌套需要转义：\'  |  \"

4. 索引取值
s4 = 'oldboy'
i) 正向取值从0开始：s4[0]
ii) 逆向取值从-1开始：s4[-1]

5. 切片(顾头不顾尾，切片有步长)
s5 = 'my love'
语法：[起始索引:结束索引:步长]
i) 步长省略，默认为1
ii) 起始索引省略，默认为从头开始
iii) 结束索引省略，默认到最后结束

了解：逆向取值，起始索引与步长为负值情况下

6. 长度
s6 = 'oldboy'
print(len(s6))
print(s6.__len__())

7. 成员运算
语法：in | not in：子字符串是否在父字符串中
'he' in 'hello'

8. 首尾去白
语法：strip()
' hello wolrd  '.strip()
'===login success==='.strip('=')

9. 拆分
语法：split(拆分规则, 拆分次数)
'D:\\python36\\python3.exe'.split('\\', 1)

10.纯数字判断
语法：isdigit()
'18'.isdigit()

11. 循环(迭代)
s10 = 'hello wolrd'

count = 0
while count < len(s10):
	print(s10[count])
	count += 1
	
for s in s10:
	print(s)
'''

'''
总结：
1. 只可以存放一个值：s = 'abc'
2. 为不可变类：s = 'xyz'
'''

''' ***
1. lstrip | rstrip：左 | 右 取留白

2. rsplit：从右开始拆分

3. lower | upper：全小 | 大写

4. startswith | endswith：以某某开头 | 结尾

5. format：格式化
'name:{}，age:{}'.format('Owen', 16)
'name:{0}，age:{1}'.format('Owen', 16)
'name:{name}，age:{age}'.format(name='Owen', age=16)

6. replace：替换
语法：replace(oldS, newS, count)
'''

''' *
1. find | rfind：查找子字符串索引，无结果返回-1

2. index | rindex：查找子字符串索引，无结果抛出异常

3. count：计算子字符串个数

4. center | ljust | rjust | zfill：按位填充
语法：center(所占位数, '填充符号')

5. expandtabs：规定\t所占空格数

6. captialize | title | swapcase：首字母大写 | 单词首字母大写 | 大小写反转

7. isdigit | isdecimal | isnumeric：数字判断

8. isalnum | isalpha：是否由字母数字组成 | 由字母组成

9. isidentifier：是否包含关键字

10. islower | isupper：是否全小 | 大写

11. isspace：是否是空白字符

12. istitle：是否为单词首字母大写格式
'''

'''
了解：字符串运算
'''
```



## 列表

```python
''' *****
1. 声明：可以包含不同类型数据，可以嵌套，[]

2. 索引取值：支持正向反向

3. 切片(顾头不顾尾，切片有步长)

4. 长度

5. 成员运算

6. 增删改
list = [1, 2, 3, 4, 5]
增：append(obj) | insert(index, obj)
删：remove(obj) | del(list[index]) | pop(index)
改：list[index] = newObj

7. 循环

8. 反转
语法：reverse()

9. 排序
语法：sort(reverse=True)

'''

'''
总结：
1. 可以存放多个值：list = [1, 2, 3]
2. 为可变类型：list.append(4)
3. 有序存储：排列的索引取值
'''

''' ***
1. copy：复制

2. clear：清空

3. count：计算成员个数

4. extend：添加多个值(参数为可迭代对象)

5. index：查找索引
'''

'''
了解：列表的运算
'''
```



## 元组

```python
'''
1. 声明：可以包含不同类型数据，可以嵌套，()

2. 索引取值：支持正向反向
'''

'''
总结：
1. 可以存放多个值：t = (1, 2, 3)
2. 为不可变类型
3. 有序存储：排列的索引取值
'''
```



## 字典：

```python
'''
1. 声明：key为不可变类型数据，value可以为任意类型，{}
d1 = {'name': 'Owen'}
d2 = dict(name='Owen')
d3 = dict([('name','Owen')])
d4 = {}.fromkeys(['name'], None)

2. 增删改查
增：d2['newKey'] = value
删：pop('key', defalutValue)
改：d2['key'] = newValue
查：d1['key']
了解：popitem()：从末尾开始删除，返回(key, value)

3. 长度：len

4. 成员运算：in | not in

5. 循环
i) 直接for循环
ii) keys()
iii) values()
iv) items()

6. 默认值取值：get
语法：get(key, defalutValue)

7. 更新
{'name': 'owen'}.update({'name': 'Owen', age: 18})

8. 设置默认
语法：setdefault(key, defalutValue)
'''

'''
总结：
1. 可以存放多个值：dic = {'name': 'Owen', age: 18}
2. 为不可变类型
3. 无序存储：安装key取值
'''
```



## 集合

```python
'''
1. 声明：
s = {1, 2, 3, 4, 5}

2. 集合运算
&交集 | |合集 | ^对称差集 | -差集 | 比较
'''
```

