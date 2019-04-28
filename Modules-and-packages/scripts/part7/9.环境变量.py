# 默认第一个路径为当前执行文件所在的路径
import sys
print(sys.path)

sys.path.clear()

print(sys.path)

# import json
# print(json)
# import socket
# print(socket)
# from json import dump

# D:\\Python36\\lib\\json
# D:\python周末四期\week6_0427\代码\part7
# sys.path.insert(0, r'D:\Python36\lib')
sys.path.append(r'D:\python周末四期\day06\代码\part7')
# sys.path.insert(0, r'D:\python周末四期\week6_0427\代码\parts7')
print(sys.path)
import json
print(json)


# import 和 from...import两种导入方式都是采用绝对路径方式导入,
# 参考的绝对路径就是环境变量sys.path中存放的路径
sys.path.append(r'D:\python周末四期\day06\代码\part6')
import m1
print(m1)

sys.path.insert(0, '123')
print(sys.path)
import my_time
