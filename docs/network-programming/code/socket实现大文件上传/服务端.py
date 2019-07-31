import socket
import struct
import json
from socket import SOL_SOCKET,SO_REUSEADDR


server = socket.socket()
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

conn,addr = server.accept()
# 先收4个长度报头
header = conn.recv(4)
# 获取字典长度
dic_len = struct.unpack('i',header)[0]
# 接收字典
dic_bytes = conn.recv(dic_len)
real_dic = json.loads(dic_bytes.decode('utf-8'))
# 获取文件相关信息
file_name = real_dic.get('file_name')
total_size = real_dic.get("file_size")
with open(file_name,'wb') as f:
    # 循环接收文件
    recv_size = 0
    while recv_size < total_size:
        data = conn.recv(1024)
        f.write(data)
        recv_size += len(data)
    print('文件上传成功')
