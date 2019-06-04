import socket


server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',8080))

while True:
    data, addr = server.recvfrom(1024)
    print(data.decode('utf-8'))
    server.sendto(data.upper(),addr)







