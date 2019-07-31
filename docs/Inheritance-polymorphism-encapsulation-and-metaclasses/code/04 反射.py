# 通过字符串来操作对象的属性或方法
class User:
    school = 'oldgirl'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def func(self):
        print('func')

# hasattr判断对象是否有某个属性或方法
# print(User.school)
# # print('school' in User.__dict__)
# print('xxx' in User.__dict__)
# # print(hasattr(User,'school'))
# print(hasattr(User,'xxx'))
# print(hasattr(User,'func'))
# print('func' in User.__dict__)
# d = {'name':"jason"}
# print(d.get('password','hahahahahaha'))

# getattr
# print(getattr(User,'school'))
# print(getattr(User,'func'))
# print(User.__dict__['school'])
# print(User.__dict__['func'])
# print(getattr(User,'xxx'))
# if hasattr(User,'xxx'):
#     getattr(User,'xxx')
# print('Buqule')


# setattr
# obj = User('jason',18)
# setattr(obj,'gender','male')  # obj.gender = 'male'
# print(obj.__dict__)


# delattr
# delattr(User,'school')
# print(User.__dict__)

class Ftp:
    def get(self):
        print('get')

    def put(self):
        print('put')

    def post(self):
        print('post')


    def run(self):
        while True:
            cmd = input('please input your cmd>>>:').strip()
            if hasattr(self,cmd):
                method = getattr(self,cmd)
                method()
            else:
                print('当前命令不存在')


obj = Ftp()
obj.run()









