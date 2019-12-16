#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import t1
# print(dir(t1))
for k in dir(t1):
    if k.isupper():
        print(k)
        v = getattr(t1,k)
    # print(k)
        print(v)




import subprocess
res = subprocess.getoutput('ifconfig')
ipinfo = res[1:3]
print(ipinfo)

import requests
r = requests.post('http://127.0.0.1:8000/api/',data=ipinfo)

print(r.text)