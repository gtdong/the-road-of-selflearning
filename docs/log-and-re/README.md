## 复习

```python
'''
ATM:
	-- start.py
		BASE_DIR = os.path.dirname(__file__)
		sys.path.append(BASE_DIR)
	-- conf
	-- lib
	-- core
	-- log
	-- db
	-- interface
	
模块：一系列功能的集合体
# 1.编译形成pyc 2.执行模块，产生名称空间存放模块的名字 3.在导包的文件中产生一个名字指向模块的名称空间

包：一系列模块的集合体
import 包名  # => 走的就是包中__init__.py
'''

'''
时间
系统
'''
```



## random模块

```python
'''
(0, 1)：random.random()
[1, 10]：random.randint(1, 10)
[1, 10)：random.randrange(1, 10)
(1, 10)：random.uniform(1, 10)
单例集合随机选择1个：random.choice(item)
单例集合随机选择n个：random.sample(item, n)
洗牌单列集合：random.shuffle(item)
'''
import random
print(random)

# for i in range(10):
#     print(random.random())  # (0, 1)


# for i in range(10):
#     print(random.randint(1, 10))  # [1, 10]

# for i in range(10):
#     print(random.randrange(1, 10))  # [1, 9]  [1, 10)

for i in range(10):
    print('%.2f' % random.uniform(1, 10))  # 小数：(1, 10)


ls = [1, 2, 3, 4, 5]
print(random.shuffle(ls))
print(ls)

print(random.choice(ls))

print(random.sample(ls, 3))


# 验证码
def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        c1 = chr(random.randint(65, 90))
        c2 = chr(random.randint(97, 122))
        c3 = str(random.randint(0, 9))
        code += random.choice([c1, c2, c3])
    return code

print(get_code(18))



def get_code(count):
    code = ""
    # 能产生大小写字母与数字
    # 进行字符串拼接
    for i in range(count):
        r = random.choice([1, 2, 3])
        if r == 1:
            c = chr(random.randint(65, 90))
        elif r == 2:
            c = chr(random.randint(97, 122))
        else:
            c = str(random.randint(0, 9))
        code += c
    return code
print(get_code(18))


def get_code(count):
    target = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    code_list = random.sample(target, count)
    return ''.join(code_list)

print(get_code(6))
```



## 序列化模块

```python
# 什么是序列化：将对象转化为字符串
# 什么是反序列化：将字符串转化为对象
# 为什么要序列化：数据的存储和传输都采用的是字符串类型
# 序列化的模块：json pickle shelve

# json：支持跨语言，用于数据的传输
# pickle：支持py的所有数据类型，所有可以将所有py的对象序列化后存储
# shelve：支持py的所有数据类型，可以即时存于取

# 序列化
dump
dumps

# 反序列化
load
loads
```



## json模块: 用于传输（多语言支持）

```python
'''
什么是json：就是完成文本序列化得到的文本字符串，json字符串具有一定的语法规范
'''

'''
1.支持的数据类型：int float str bool dict list null
2.复杂的json都是由{}与[]嵌套形成的数据
3.json字符串只能有一个根: json_str = '{}{}' | '{}[]' | '[][]' | '1null'  # 报错，都是两个根
4.json中的str类型必须用""包裹(json字符串中的字符串类型不支持'' """""")
'''

# python对象 序列化 json字符串
data = None
res = json.dumps(data)
print(res)

# json字符串 反序列化 python对象
json_str = '3.14'
json_str = 'true'
json_str = 'null'
json_str = '{}'
json_str = '[]'
json_str = '1, null'  # 有误，两个根
# str类型，json只支持""
json_str = "\"abc\""
json_str = '"abc"'
obj = json.loads(json_str)
print(obj, type(obj))

# 操作文件
# 序列化
obj = {'name': 'Owen', 'age': 17, 'gender': '男'}

with open('a.txt', 'w', encoding='utf-8') as wf:
    json.dump(obj, wf, ensure_ascii=False)
    # json.dump(obj, wf, ensure_ascii=False)
    # wf.write('123')
    # wf.write('456')

# 反序列化
with open('a.txt', 'r', encoding='utf-8') as rf:
    obj = json.load(rf)
    print(obj)
    

print(json.load(open('a.txt', 'r', encoding='utf-8')))

# 注：json模块的序列化与反序列化是一一对应关系
```



## pickle模块：支持所有数据类型

```python
import pickle

# 序列化
obj = {'name': 'Owen', 'age': 17, 'gender': '男'}
res = pickle.dumps(obj)
print(res)

pickle.dump(obj, open('b.txt', 'wb'))


# 反序列化
print(pickle.loads(res))
print(pickle.load(open('b.txt', 'rb')))
```



## shelve模块：支持所有数据类型，即时存取

```python
import shelve

shv_tool = shelve.open('c.shv')

# 序列化
shv_tool['name'] = 'Owen'

# 反序列化
res = shv_tool['name']
print(res)
# 文件通过shelve对象来关闭
shv_tool.close()


# writeback将反序列化到内存的数据，操作后即时同步到文件中
with shelve.open('c.shv', writeback=True) as shv_tool:
    shv_tool['stus'] = ['Bob', 'Tom']
    # print(shv_tool['stus'])

    shv_tool['stus'].append('Jobs')
    print(shv_tool['stus'])
```



## shutil：可以操作权限的处理文件模块

```python
# 基于路径的文件复制：
shutil.copyfile('source_file', 'target_file')

# 基于流的文件复制：
with open('source_file', 'rb') as r, open('target_file', 'wb') as w:
    shutil.copyfileobj(r, w)
    
# 递归删除目标目录
shutil.rmtree('target_folder')

# 文件移动
shutil.remove('old_file', 'new_file')

# 文件夹压缩
# file_name: 压缩后得到的文件名  format：压缩格式  archive_path：要压缩的文件夹路径
shutil.make_archive('file_name', 'format', 'archive_path')

# 文件夹解压
# unpack_file: 解压的文件  unpack_name：解压得到的文件夹名  format：解压格式
shutil.unpack_archive('unpack_file', 'unpack_name', 'format')
```



## 加密模块

### hashlib模块

```python


# 加盐
# 什么是加盐：在原数据前或后添加一些预定的数据，与原数据一起进行加密
# 为什么要加盐：
# 1.当原数据过于简单，可以对其加盐，提高数据的复杂度
# 2.盐与数据有一定相似度，混淆对真实数据的提取
lock_obj = hashlib.md5()  # 生产锁对象可以添加数据参数也可以省略
lock_obj.update(b'before_salt')
lock_obj.update('要被加密的数据'.encode('utf-8'))
lock_obj.update(b'after_salt')
print(lock_obj.hexdigest())


# 注：要为新数据提供加密，一定要为该数据创建一个加密对象

# 其他算法
lock_obj = hashlib.sha3_256(b'123')
print(lock_obj.hexdigest())
lock_obj = hashlib.sha3_512(b'123')
lock_obj.update(b'salt')
print(lock_obj.hexdigest())

```



## hmac模块

```python
import hmac
# 与hashlib的不同点：生产锁对象时必须提高数据参数
lock_obj = hmac.new(b'')
print(lock_obj.hexdigest())

lock_obj = hmac.new(b'')
lock_obj.update(b'salt')
print(lock_obj.hexdigest())
```



## logging模块

```python
# logging记录项目日志的模块
# 记录日志：将项目中产生的一些数据，或是信息，或是错误不再输出到控制台，而是输出到文件中，保存这样信息的文件就称之为日志文件
```

## 基本使用

```python
import logging
import sys

# 2.日志的基本配置
logging.basicConfig(
    # 输出级别
    # level=logging.INFO,
    level=10,

    # 输出位置
    stream=sys.stderr,  # sys.stdout  往控制台输出
    # filename='log/my.log',  # 往文件输出  => 如果需要同时往多个位置输出，需要handles

    # 输出格式
    format='%(asctime)s: %(msg)s',
    datefmt='%H:%M:%S'
)


# 1.五大级别
logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
# logging.warn('warning msg')  # 弃用
logging.error('error msg')
logging.critical('critical msg')
logging.fatal('critical msg')  # 同critical
```



## 成员组成

```python
import logging

# 1.打印者：自定义的打印者如何配置
log1 = logging.getLogger('logger name')

# 2.输出位置：两个文件输出位置与一个控制台输出位置
hd_a = logging.FileHandler('log/a.log', encoding='utf-8')
hd_cmd = logging.StreamHandler()

# 3.输出格式
fmt1 = logging.Formatter('%(asctime)s 【%(name)s】- %(msg)s')
fmt2 = logging.Formatter('%(asctime)s - %(msg)s')

# 4.打印者添加句柄 - 设置打印者的输出位置
log1.addHandler(hd_a)
log1.addHandler(hd_cmd)

# 5.将格式绑定给输出位置(句柄)
hd_a.setFormatter(fmt1)
hd_cmd.setFormatter(fmt2)

# 6.权限控制
log1.setLevel(logging.DEBUG)  # 打印者规定打印级别
hd_a.setLevel(logging.WARNING)  # 不同输出位置(句柄)再可以二次限定输出级别
hd_cmd.setLevel(logging.DEBUG)  # 不同输出位置(句柄)再可以二次限定输出级别

# 7.不同级别输出信息
log1.debug('debug msg')
log1.info('info msg')
log1.warning('warning msg')
log1.error('error msg')
log1.critical('critical msg')
```



## logging配置文件的项目运用

```python
# 1.将打印者，句柄，与格式封装成配置信息
# 2.加载配置信息
# 3.使用自定义logger，采用的就是配置信息设置的logger

# 优势：1，2两步是一劳永逸的，后期开发只需要在要记录日志的文件中使用自定义logger



# 一、配置
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'o_fmt1': {
            'format': '%(asctime)s 【%(name)s】- %(msg)s'
        },
        'o_fmt2': {
            'format': '%(asctime)s - %(msg)s'
        }
    },
    'filters': {},
    'handlers': {
        'o_hd_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',  # 打印到控制台
            'formatter': 'o_fmt1',
            'filename': 'log/sys.log',
            'encoding': 'utf-8',
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
        },
        'o_hd_cmd': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到控制台
            'formatter': 'o_fmt2'
        }
    },
    'loggers': {
        'o_owen': {
            'level': 'DEBUG',
            'handlers': ['o_hd_file', 'o_hd_cmd']
        },
        'o_zero': {
            'level': 'DEBUG',
            'handlers': ['o_hd_cmd'],
            # 'propagate': True  # 向上传递
        }
    }
}

# 二、加载配置
import logging.config
logging.config.dictConfig(LOGGING_DIC)


# 三、使用
log = logging.getLogger('o_zero')
log.critical('信息')

log1 = logging.getLogger('o_owen')
log1.critical('信息')
```



## re模块

```python
# re：正则，全称正则字符串 - re就是有特殊语法的字符串
# re可以将有正则语法的字符串解析为对应的正则对象，用来匹配目标字符串

# 学习re的目的：1.判断目标字符串是否合法 2.在目标字符串中提取想要的信息（信息匹配规则采用正则）


# 基本使用

import re

r1 = re.findall(r'1', '123abc123')
print(r1)

# re.I不区分大小写匹配
r2 = re.findall(r'a', '123abc123ABC', flags=re.I)
print(r2)

# 1.将 r'\d' 丢给_compile得到可以匹配数字的 正则对象
# 2.正则对象.findall('目标字符串')
r3 = re.findall(r'\d', '123abc123')
print(r3)


re_obj = re.compile(r'\d')  # 将 r'\d' 丢给_compile得到可以匹配数字的 正则对象
r4 = re_obj.findall('123abc123')  # 正则对象.findall('目标字符串')
print(r4)
```



## 单个字符

```python
# 一、单个字符语法
# 匹配a
print(re.findall(r'a', '123abc嘿嘿'))  # ['a']

# a或b
print(re.findall(r'a|b', '123abc嘿嘿'))  # ['a', 'b'] 不建议使用
print(re.findall(r'[ab]', '123abc嘿嘿'))  # ['a', 'b'] 建议使用

# 非a非b
print(re.findall(r'[^ab]', '123abc嘿嘿'))  # ['1', '2', '3', 'c', '嘿', '嘿']

# 数字
print(re.findall(r'[0-9]', '12abc嘿嘿12'))  # ['1', '2', '1', '2'] 建议使用
print(re.findall(r'\d', '12abc嘿嘿12'))  # ['1', '2', '1', '2'] 不建议使用

# 字母
print(re.findall(r'[a-zA-Z]', '12abc[嘿嘿ABC'))  # ['a', 'b', 'c', 'A', 'B', 'C']

# 字母数字_常用汉字：\w => 建议使用 [a-zA-Z0-9_]
print(re.findall(r'\w', '12abc[_嘿嘿ABC'))  # ['1', '2', 'a', 'b', 'c', '_', '嘿', '嘿', 'A', 'B', 'C']

# 汉字 [\u4e00-\u9fa5]
print(re.findall(r'[\u4e00-\u9fa5]', '12abc[_嘿嘿ABC'))  # ['嘿', '嘿']

# 空白字符：\s => 建议使用[ \f\n\r\t\v]
print(re.findall(r'\s', ' \f\n\r\t\v'))  # [' ', '\x0c', '\n', '\r', '\t', '\x0b']

# 非\n的任意字符: .
print(re.findall(r'.', ' \f\n\r\t\v*&_.'))  # [' ', '\x0c', '\r', '\t', '\x0b', '*', '&', '_', '.']

# 只想匹配.字符：\.
print(re.findall(r'\.', ' \f\n\r\t\v*&_.'))  # ['.']

# re.S: 让.也能匹配\n，就可以理解为 . 可以匹配所有字符
print(re.findall(r'.', ' \f\n\r\t\v*&_.', flags=re.S))

# 取对立面 \d数字 \D非数字  \w=>\W  \s=>\S
print(re.findall(r'\D', '12abc\f嘿嘿12'))  # ['a', 'b', 'c', '\x0c', '嘿', '嘿']

```



## 重复字符语法

```python
# 二、重复字符语法
print(re.findall(r'ab', 'abacbabc'))  # ['ab', 'ab']

# 指定个数: 匹配abb
print(re.findall(r'ab{2}', 'aababbabbb'))  # ['abb', 'abb']

# 贪婪匹配: 尽可能多的匹配
# a0~2个b: a | ab | abb
print(re.findall(r'ab{,2}', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abb']

# a0~n个b:
print(re.findall(r'ab{0,}', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abbb']

# a1~3个b:
print(re.findall(r'ab{1,3}', 'aababbabbb'))  # ['ab', 'abb', 'abbb']

# *: {0,}
print(re.findall(r'ab*', 'aababbabbb'))  # ['a', 'ab', 'abb', 'abbb']
# +: {1,}
print(re.findall(r'ab+', 'aababbabbb'))  # ['ab', 'abb', 'abbb']
# ?: {,1}
print(re.findall(r'ab?', 'aababbabbb'))  # ['a', 'ab', 'ab', 'ab']

# 非贪婪匹配
print(re.findall(r'ab{1,3}?', 'aababbabbb'))  # ['ab', 'ab', 'ab']

# 重点：非贪婪匹配应用场景，一般都是结合有开头与结尾的标识
print(re.findall(r'<.{1,}>', '<a><b>msg</b></a>'))  # ['<a><b>msg</b></a>']
# 匹配标签
print(re.findall(r'<.{1,}?>', '<a><b>msg</b></a>'))  # ['<a>', '<b>', '</b>', '</a>']

# *?: {0,}?
# +?: {1,}?
# ??: {,1}?
print(re.findall(r'<.+?>', '<a><b>msg</b></a>'))  # ['<a>', '<b>', '</b>', '</a>']

```



## 分组语法

```python

# 引子
print(re.findall(r'(?:ab){2}', 'abbabab'))  # ['abab']

# findall(): 没有分组情况下，显示匹配的结果；如果有分组，显示分组结果

# 分组：()
# 取消分组：(?:)
# 有名分组：(?P<名字>)

# 案例：
# 匹配链接
print(re.findall(r'www\..+?\.com', 'www.baidu.comabcwww.sina.com'))  # ['www.baidu.com', 'www.sina.com']
# 获取链接的域名：['baidu', 'sina']
print(re.findall(r'www\.(.+?)\.com', 'www.baidu.comabcwww.sina.com'))  # ['baidu', 'sina']

# 分组编号: 从左往右数左(进行分组编号
# [('www.baidu.com', 'baidu', 'com'), ('www.sina.edu', 'sina', 'edu')]
res = re.findall(r'(www\.(.+?)\.(com|edu))', 'www.baidu.comabcwww.sina.edu')
print(res)
print(res[0][1])

# 取消分组:(?:) 应用于，要将一些数据作为整体看待，但由不能产生分组
# [('www.baidu.com', 'baidu'), ('www.sina.edu', 'sina')]
res = re.findall(r'(www\.(.+?)\.(?:com|edu))', 'www.baidu.comabcwww.sina.edu')
print(res)
```



## 正则其他方法

```python
# match:不是全文匹配，必须从头开始匹配，且只匹配一次
res = re.match(r'(www\.(?P<site_name>.+?)\.(?:com|edu))', 'www.baidu.comwww.sina.edu')
# 可以通过分组号直接取出分组内容
print(res.group(1))
print(res.group(2))
# print(res.group(0), res)  # 匹配的整体

# 有名分组
print(res.group('site_name'))


# split(): 拆分
print('abc def xyz'.split(' '))
print(re.split(r' ', 'abc def xyz'))
print(re.split(r'[,@ ]', 'abc,def@xyz opq'))


# sub(): 替换
res = re.sub(r'good', 'bed', 'good good day a')
print(res)  # bed bed day a

res = re.sub(r'good', 'bed', 'good good day a', count=1)
print(res)  # bed good day a

res = re.sub(r'good day a', '123', 'good day a!!!')
print(res)  # 123!!!

# 结合分组可以完成数据的重组
res = re.sub(r'(good) (day) (a)', r'today is \3 \1 \2', 'good day a!!!')
print(res)  # today is a good day!!!
```





















