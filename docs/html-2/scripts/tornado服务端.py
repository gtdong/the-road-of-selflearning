import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument('username')
        pwd = self.get_argument('pwd')
        print(username, pwd)
        if username == 'zekai' and pwd == '123qwe':
            print('登陆成功')
        self.write("Hello, world")

    def post(self):

        # username  =self.get_body_argument('username')
        # pwd = self.get_body_argument('pwd')
        # print(username, pwd)
        # hobby = self.get_body_arguments('hobby')
        # gender = self.get_body_argument('gender')
        # print(gender)
        # token = self.get_body_argument('token')
        # print(token)

        city = self.get_body_argument('city')
        print(city)

        self.write('this is a test')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()