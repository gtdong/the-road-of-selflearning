from db import db_handler
from lib import common

# 获取用户日志功能
user_logger = common.get_logger('user')

# 注册接口
def register_interface(user, pwd):

    user_dict = db_handler.select(user)

    if user_dict:
        return False, '用户已存在'

    # 业务逻辑
    user_dic = {
        'name': user,
        'pwd': pwd,
        'balance': 15000,
        'flow': [],
        'shopping_car': {}
    }

    db_handler.save(user_dic)

    user_logger.info('%s注册成功' % user)

    return True, '%s注册成功' % user


# 登录接口
def login_interface(user, pwd):
    # None or 用户字典
    user_dic = db_handler.select(user)

    # 用户不存在，返回False
    if not user_dic:
        return False, '用户不存在！'

    if pwd == user_dic['pwd']:
        return True, '登陆成功!'
    else:
        return False, '密码错误'


# 查看余额接口
def check_bal_interface(user):
    user_dic = db_handler.select(user)
    return user_dic['balance']