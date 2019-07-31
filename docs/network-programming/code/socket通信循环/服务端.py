import socket

"""
服务端
1.24小时不间断提供服务端
2.有固定的ip和port
3.支持高并发

并发:只要看起来像同时进行就可以称之为并发
并行:真正意义上的同时执行
"""
server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)


conn, addr = server.accept()
while True:
    try:
        data = conn.recv(1024)  # b''
        if len(data) == 0:break  # 针对mac linux系统而言
        print(data)
        conn.send(data.upper())
    except ConnectionResetError:
        break

conn.close()
server.close()






