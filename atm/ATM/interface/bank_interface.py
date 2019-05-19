'''
银行接口
'''
from db import db_handler
from lib import common

# 获取银行日志功能
bank_logger = common.get_logger('bank')

# 提现接口
def withdraw_interface(user, money):
    user_dic = db_handler.select(user)

    money2 = money

    money *= 1.05

    if user_dic['balance'] >= money:
        user_dic['balance'] -= money

        user_dic['flow'].append('%s提现%s元成功!' % (user, money2))

        db_handler.save(user_dic)

        bank_logger.info('%s提现%s元成功!' % (user, money2))

        return True, '%s提现%s元成功!' % (user, money2)

    return False, '*穷*，去充钱!'


# 转账接口
def transfer_interface(from_user, to_user, money):
    # 目标用户信息
    to_user_dic = db_handler.select(to_user)

    # 判断目标用户是否存在
    if not to_user_dic:
        return False, '目标用户不存在!'

    # 获取当前用户信息
    from_user_dic = db_handler.select(from_user)

    if from_user_dic['balance'] >= money:
        to_user_dic['balance'] += money

        from_user_dic['balance'] -= money

        # 给当前用户记录流水
        from_user_dic['flow'].append('%s向%s转账%s元!' % (from_user, to_user, money))

        # 给目标用户记录流水
        to_user_dic['flow'].append('%s接收%s转账%s元!' % (to_user, from_user, money))

        # 保存用户信息
        db_handler.save(from_user_dic)
        db_handler.save(to_user_dic)

        return True, '转账成功!'

    return False, '用户金额不足!'


# 还款接口
def repay_interface(user, money):
    user_dic = db_handler.select(user)
    user_dic['balance'] += money
    db_handler.save(user_dic)
    return '还款成功!'


# 流水接口
def flow_interface(user):
    user_dic = db_handler.select(user)
    return user_dic['flow']


# 支付接口
def pay_money_interface(user, cost):
    user_dic = db_handler.select(user)

    user_dic['balance'] -= cost

    db_handler.save(user_dic)

    return True, '支付成功'
