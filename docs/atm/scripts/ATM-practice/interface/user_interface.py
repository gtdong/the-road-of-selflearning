#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong

from db import db_handler


def register_interface(user, pwd):
    user_dict = db_handler.select(user)
    if user_dict:
        return False, '用户已存在，请登录'

    user_dic = {
        'name': user,
        'pwd': pwd,
        'balance': 15000,
        'flow': [],
        'shopping_car': {}
    }

    db_handler.save(user_dic)
    return True, '注册成功'


def login_interface(user, pwd):
    user_dict = db_handler.select(user)
    if not user_dict:
        return False, '用户不存在'
    if pwd == user_dict['pwd']:
        return True, '登录成功！'
    else:
        return False, '登录失败！'

def check_bal_interface(user):
    user_dict = db_handler.select(user)
    return user_dict['balance']
