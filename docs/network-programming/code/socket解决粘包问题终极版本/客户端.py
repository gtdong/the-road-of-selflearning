import socket
import struct
import json

client = socket.socket()
client.connect(('127.0.0.1',8080))


while True:
    cmd = input('please input your cmd>>>:').encode('utf-8')
    if len(cmd) == 0:continue
    client.send(cmd)
    # 先接收报头
    header = client.recv(4)
    # 解析获取字典的长度
    dic_len = struct.unpack('i',header)[0]
    dic_bytes = client.recv(dic_len)
    real_dic = json.loads(dic_bytes.decode('utf-8'))
    print(real_dic)
    # 循环接收真实数据
    data = b''
    recv_size = 0
    while recv_size < real_dic['total_size']:
        info = client.recv(1024)
        data += info
        recv_size += len(info)
    print(data.decode('gbk'))



