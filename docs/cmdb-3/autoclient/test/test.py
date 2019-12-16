import requests

key = "skfngksdgnfkjdsgnfdskjgs"


#### 第一种方式
# res = requests.get('http://127.0.0.1:8000/api/',headers={'key':key})
# print(res.text)


#### 第二种方式

import hashlib,time

client_time = time.time()

tmp = "%s|%s" % (key,client_time)

m = hashlib.md5()
m.update(bytes(tmp,encoding='utf8'))
res = m.hexdigest()
#
info = "%s|%s" % (res,client_time)
#
print(info)
# res = requests.get('http://127.0.0.1:8000/api/',headers={'key':info})
# print(res.text)
res = requests.get('http://127.0.0.1:8000/asset/',headers={'key':info})
print(res.text)