import socket
import struct

client = socket.socket()
client.connect(('127.0.0.1',8080))


while True:
    cmd = input('please input your cmd>>>:').encode('utf-8')
    if len(cmd) == 0:continue
    client.send(cmd)
    # 先接收报头
    header = client.recv(4)
    # 解析真实数据长度
    total_size = struct.unpack('i',header)[0]
    # 循环接收真实数据
    data = b''
    recv_size = 0
    while recv_size < total_size:
        info = client.recv(1024)
        data += info
        recv_size += len(info)
    print(data.decode('gbk'))



