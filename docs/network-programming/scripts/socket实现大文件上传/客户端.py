import socket
import struct
import json
import os





client = socket.socket()
client.connect(('127.0.0.1',8080))


file_path = r'D:\python周末四期\day11\1.时间模块.mp4'
file_size = os.path.getsize(file_path)  # 获取文件大小
send_dic = {"file_name":'FBI warning','file_info':"注意身体",'file_size':file_size}
send_bytes = json.dumps(send_dic).encode('utf-8')
# 制作报头
head = struct.pack('i',len(send_bytes))
# 发送报头
client.send(head)
# 发字典
client.send(send_bytes)
# 发文件
with open(file_path,'rb') as f:
    for line in f:
        client.send(line)



