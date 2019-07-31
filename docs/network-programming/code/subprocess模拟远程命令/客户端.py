import socket


client = socket.socket()
client.connect(('127.0.0.1',8080))


while True:
    cmd = input('please input your cmd>>>:').encode('utf-8')
    if len(cmd) == 0:continue
    client.send(cmd)
    data = client.recv(1024)
    print(data.decode('gbk'))



