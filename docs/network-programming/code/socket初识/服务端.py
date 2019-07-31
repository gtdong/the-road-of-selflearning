import socket

server = socket.socket()  # 买手机   不传参数默认就是TCP协议
server.bind(('127.0.0.1', 8080))  # 插手机卡
server.listen(5)  # 半连接池


conn, addr = server.accept()  # 待机  阻塞

data = conn.recv(1024)  # 听别人说话   接收1024个bytes
print(data)
conn.send(b'hello big baby~')  # 回话


conn.close()  # 挂电话
server.close()  # 关机







