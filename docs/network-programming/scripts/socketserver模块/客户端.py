import socket
import time

client = socket.socket()
client.connect(('127.0.0.1',8080))

while True:
    client.send(b'hello')
    data = client.recv(1024)
    print(data)
    time.sleep(1)