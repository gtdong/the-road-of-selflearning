import socketserver


class MyBaby(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                print(data)
                self.request.send(data.upper())
            except ConnectionResetError:
                break


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyBaby)
    server.serve_forever()