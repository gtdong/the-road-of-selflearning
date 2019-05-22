#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import db_handler
from lib import common


def withdraw_interface(user, money):
    user_dict = db_handler.select(user)

    money2 = money

    money *= 1.05
    if user_dict['balance'] >= money:
        user_dict['balance'] -= money

        user_dict['flow'].append("%s提现%s元成功" % (user, money2))

        db_handler.save(user_dict)
        return True, '%s提现%s元成功！' % (user, money2)
        return False, '穷，去充钱！'


def transfer_interface(from_user, to_user, money):
    to_user_dic = db_handler.select(to_user)
    if not to_user_dic:
        return False, '用户不存在'

    from_user_dic = db_handler.select(from_user)

    if from_user_dic['balance'] >= money:
        to_user_dic['balance'] += money
        from_user_dic['balance'] -= money

        to_user_dic['flow'].append('%s向%s转账%s元' % (from_user, to_user, money))
        from_user_dic['flow'].append('%s向%s转账%s元' % (from_user, to_user, money))

        db_handler.save(from_user_dic)
        db_handler.save(to_user_dic)

        return True, '转帐成功!'

    return False, '用户金额不足！'


def repay_interface(user, money):
    user_dic = db_handler.select(user)
    user_dic['balance'] += money
    db_handler.save(user_dic)
    return '还款成功！'

def flow_interface(user):
    user_dic = db_handler.select(user)
    return user_dic['flow']

def pay_money_interface(user, cost):
    user_dic = db_handler.select(user)

    user_dic['balance'] -= cost

    db_handler.save(user_dic)

    return True, '支付成功'
