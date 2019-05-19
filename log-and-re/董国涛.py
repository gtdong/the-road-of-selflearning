#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong

#1
import re
str1 = "^" + "\\d{6}" + "(18|19|([23]\\d))\\d{2}" + "((0[1-9])|(10|11|12))" + "(([0-2][1-9])|10|20|30|31)" + "\\d{3}" + "[0-9Xx]" + "$"
# strData = input("请输入您的身份证号:")
pattern = r'^\d{6}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
res = re.match(pattern,'321183399410184854')
print(res)



#2

import requests
res = requests.get('https://www.baidu.com')  # 获取主页
ctx = res.content.decode('utf-8')  # 解析得到主页内容
pattern= r'www.baidu.com/[^\s]+\.(?:gif|png)'
print(re.findall(pattern,ctx))
