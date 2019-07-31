import socket


client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:
    msg = input('please input your msg>>>:').encode('utf-8')
    if len(msg) == 0:continue
    client.send(msg)
    data = client.recv(1024)
    print(data)

