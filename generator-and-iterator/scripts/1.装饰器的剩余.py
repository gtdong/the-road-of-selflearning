'''
def huaping():
    pass

temp = huaping
def my_huaping():
    # ...
    temp()
    # ...
huaping = my_huaping
huaping()


# 为登录功能添加账号检验功能：必须是3个及以上英文字母组成
def check_user(func):
    def inner(*args, **kwargs):
        user = args[0]
        if not (user.isalpha() and len(user) >= 3):
            return '账号不合法'
        res = func(user, pwd)
        return res
    return inner

# 为登录功能添加密码检验功能：必须是3个及以上英文字母或数字组成
def check_pwd(func):
    def inner(*args, **kwargs):
        pwd = args[1]
        if not (pwd.isalnum() and len(pwd) >= 3):
            return '密码不合法'
        res = func(*args, **kwargs)
        return res
    return inner

# 对登录结果的修饰装饰器：True=>登录成功 False=>登录失败
def change_res(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        if res == True:
            return '登录成功'
        return '登录失败'
    return inner


@check_user  # login = check_user(login)
@check_pwd
@change_res
def login(user, pwd):
    if user == 'owen' and pwd == '123':
        return True
    return False

user = input('user: ')
pwd = input('pwd: ')
res = login(user, pwd)
'''

# 1.带参装饰器

def wrap(num):
    def outer(func):
        print(num)
        def inner(*args, **kwargs):
            print(num)
            res = func(*args, **kwargs)
            return res
        return inner
    return outer

num = 10
# outer = wrap(num)
# @outer  # fn = outer(fn)
@wrap(num)  # @wrap(10) - @outer - fn = outer(fn) - fn = inner(新功能)
def fn():
    pass
fn()


# 2.文档注释
def fn2(num):
    '''
    :param num: 一个整数
    :return: 整数加10的结果
    '''
    return num + 10

# fn.__doc__就是打印该函数的文档注释(解释该函数功能的)
print(fn2)
print(fn2.__doc__)

# print(''.join.__doc__)

def temp():
    '''
    :return: 111111111111111
    '''
def temp1():
    '''
    :return: 22222
    '''
# 3.
from functools import wraps
def outer(func):
    # @wraps(temp)  # 将inner.__doc__指向temp的__doc__
    @wraps(func)  # 将inner.__doc__指向被装饰的func的__doc__
    def inner(*args, **kwargs):
        '''
        :param args: 被装饰函数的位置形参
        :param kwargs: 被装饰函数的关键字形参
        :return:
        '''
        res = func(*args, **kwargs)
        return res
    return inner

@outer
def fn3(arg):
    '''
    :param arg: fn3的参数
    :return:
    '''
print(fn3)  # fn3 == inner
# fn3本质是inner，但是我打印文档注释，能不能形成一个打印假象，
# 打印的是fn3自己文档注释 - 为了统一查看原码和打印文档注释，显示的是同样内容
print(fn3.__doc__)



