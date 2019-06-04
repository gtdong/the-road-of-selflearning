import socket



server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)


conn,addr = server.accept()

data = conn.recv(5)
print(data)
data = conn.recv(5)
print(data)
data = conn.recv(8)
print(data)