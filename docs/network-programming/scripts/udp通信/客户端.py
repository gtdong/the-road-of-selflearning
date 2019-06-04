import socket


client = socket.socket(type=socket.SOCK_DGRAM)
server_addr = ('127.0.0.1',8989)

msg = input('>>>:')
client.sendto(msg.encode('utf-8'),server_addr)
# client.sendto(b'xsdasd',server_addr)
# client.sendto(b'sdfsdfsfa',server_addr)
data,addr = client.recvfrom(1024)
print(data,addr)