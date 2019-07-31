# UDP socketserver使用
import socketserver


class MyUdpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            data, sock = self.request
            print(data)
            sock.sendto(data.upper(), self.client_address)


if __name__ == '__main__':
    server = socketserver.ThreadingUDPServer(('127.0.0.1', 8080), MyUdpServer)
    server.serve_forever()