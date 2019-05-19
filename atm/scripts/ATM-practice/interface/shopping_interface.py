#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import db_handler
from interface import bank_interface
from lib import common

def save_shop_car_interface(user,shopping_car):
    user_dic = db_handler.select(user)

    user_dic['shopping_car'] = shopping_car

    db_handler.save(user_dic)

    return '添加购物车成功！'

def pay_interface(user,cost):
    flag, msg = bank_interface.pay_money_interface(user,cost)
    user_dic= db_handler.select(user)
    user_dic['shopping_car'] = {}
    db_handler.save(user_dic)

    return flag,msg

def check_shop_car_interface(user):
    user_dic = db_handler.select(user)
    return user_dic['shopping_car']