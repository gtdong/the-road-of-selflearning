from db import db_handler
from interface import bank_interface
from lib import common

# 获取商城日志功能
shop_logger = common.get_logger('shop')

# 添加购物车接口
def save_shop_car_interface(user, shopping_car):
    user_dic = db_handler.select(user)

    user_dic['shopping_car'] = shopping_car

    # 添加购物车思路
    # for good in shopping_car:
        # if good in user_dic['shopping_car']:
        #     user_dic['shopping_car'][good] += shopping_car[good]
    db_handler.save(user_dic)

    shop_logger.info('%s添加购物车成功' % user)

    return '添加购物车成功'


# 结账接口
def pay_interface(user, cost):
    # (True, msg)
    flag, msg = bank_interface.pay_money_interface(user, cost)

    # 清空购物车
    user_dic = db_handler.select(user)
    user_dic['shopping_car'] = {}

    db_handler.save(user_dic)

    return flag, msg


# 查看购物车接口
def check_shop_car_interface(user):
    user_dic = db_handler.select(user)
    return user_dic['shopping_car']