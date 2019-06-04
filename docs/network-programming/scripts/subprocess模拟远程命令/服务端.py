import socket
import subprocess


server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)


while True:
    conn, addr = server.accept()
    while True:
        try:
            cmd = conn.recv(1024).decode('utf-8')
            if len(cmd) == 0:break
            obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            print(len(stdout+stderr))
            conn.send(stdout+stderr)
        except ConnectionResetError as e:
            print(e)
            break
    conn.close()
server.close()





