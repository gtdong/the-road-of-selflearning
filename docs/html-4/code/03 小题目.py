# res = 'true'
#
# import json
# res1 = json.loads(res)
# print(res1,type(res1))
class Demo(object):
    def func(self):
        print('func')
        return self

    def index(self):
        print('index')
        return self

obj = Demo()
obj.func().index()

