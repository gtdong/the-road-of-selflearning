import socket


server = socket.socket(type=socket.SOCK_DGRAM)  # UDP协议
server.bind(('127.0.0.1',8989))


data,addr = server.recvfrom(1024)
print(data,addr)
# data,addr = server.recvfrom(1024)
# print(data,addr)
# data,addr = server.recvfrom(1024)
# print(data,addr)
server.sendto(data.upper(),addr)

