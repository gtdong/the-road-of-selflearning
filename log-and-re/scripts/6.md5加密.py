# md5加密：不可逆加密
# 碰撞解密：用数据再进行一次加密，与原加密结果做匹配


import hashlib

data = '数据'
lock_obj = hashlib.md5(data.encode('utf-8'))  # 生产加密锁对象，传入加密数据
result = lock_obj.hexdigest()  # 获取加密后的加密串
print(result)


data = '数据数据数据数据数据数据数据数据数据数据数据数据'
data = ''
lock_obj = hashlib.md5(data.encode('utf-8'))  # 生产加密锁对象，传入加密数据
result = lock_obj.hexdigest()  # 获取加密后的加密串
print(result)


# update可以往锁对象中添加加密数据
lock_obj = hashlib.md5()
lock_obj.update(b'123')
lock_obj.update(b'abc')
lock_obj.update('嘿嘿'.encode('utf-8'))
print(lock_obj.hexdigest())


lock_obj.update(b'000')
print(lock_obj.hexdigest())  # 000 | '123abc嘿嘿000'.encode('utf-8')

print(hashlib.md5('123abc嘿嘿000'.encode('utf-8')).hexdigest())

# 注：要为新数据提供加密，一定要为该数据创建一个加密对象


# 加盐
# 什么是加盐：在原数据前或后添加一些预定的数据，与原数据一起进行加密
# 为什么要加盐：
# 1.当原数据过于简单，可以对其加盐，提高数据的复杂度
# 2.盐与数据有一定相似度，混淆对真实数据的提取

data = 'ab_12'
lock_obj = hashlib.md5()
lock_obj.update(b'a12_d')
lock_obj.update(data.encode('utf-8'))
lock_obj.update(b'dd_121')
print(lock_obj.hexdigest())
# a12_dab_12dd_121


# 其他位数加密
lock_obj = hashlib.sha3_256(b'123')
print(lock_obj.hexdigest())
lock_obj = hashlib.sha3_512(b'123')
lock_obj.update(b'salt')
print(lock_obj.hexdigest())


import hmac
# 与hashlib的不同点：生产锁对象时必须提高数据参数
lock_obj = hmac.new(b'')
print(lock_obj.hexdigest())

lock_obj = hmac.new(b'')
lock_obj.update(b'salt')
print(lock_obj.hexdigest())





