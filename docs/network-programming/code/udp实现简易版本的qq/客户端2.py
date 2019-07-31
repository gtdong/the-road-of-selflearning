import socket


client = socket.socket(type=socket.SOCK_DGRAM)
server_addr = ('127.0.0.1',8080)

while True:
    # msg = input('>>>:')
    # msg = '客户端3:%s'%msg
    # client.sendto(msg.encode('utf-8'),server_addr)
    client.sendto(b'hello',server_addr)

    data,addr = client.recvfrom(1024)
    print(data)


