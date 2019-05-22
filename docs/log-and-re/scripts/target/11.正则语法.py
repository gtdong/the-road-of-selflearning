import re
"""
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
"""

"""
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
"""


# 三、分组语法

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


# 四、其他正则方法的使用

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