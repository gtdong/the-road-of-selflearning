#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from interface import user_interface, bank_interface, shopping_interface
from lib import common

user_info = {'name': None}


def register():
    while True:
        user = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        re_pwd = input('请再次输入密码:').strip()

        if pwd == re_pwd:
            flag, msg = user_interface.register_interface(user, pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        break


def login():
    while True:
        user = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        flag, msg = user_interface.login_interface(user, pwd)
        if flag:
            print(msg)
            user_info['name'] = user
            break
        else:
            print(msg)


@common.login_auth
def check_balance():
    balance = user_interface.check_bal_interface(user_info['name'])
    print('尊敬的用户[%s]，您的余额为[%s]' % (user_info['name'], balance))


@common.login_auth
def withdraw():
    while True:
        money = input('请输入提现金额：').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank_interface.withdraw_interface(user_info['name'], money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.login_auth
def transfer():
    while True:
        to_user = input('请输入要转账的人：').strip()
        money = input('请输入要转帐的金额：').strip()

        if money.isdigit():
            money = int(money)

            flag, msg = bank_interface.transfer_interface(user_info['name'], to_user, money)
            if flag:
                print(msg)
                break
            else:
                print(msg)


@common.login_auth
def repay():
    while True:
        money = input('请输入你要还款的金额：').strip()
        if money.isdigit():
            money = int(money)

            msg = bank_interface.repay_interface(user_info['name'], money)

            print(msg)
            break
        else:
            print('请输入数字：')


@common.login_auth
def check_flow():
    flow_list = bank_interface.flow_interface(user_info['name'])
    for flow in flow_list:
        print(flow)


@common.login_auth
def shopping_car():
    user_balance = user_interface.check_bal_interface(user_info['name'])

    shopping_cars = {}

    cost = 0

    while True:
        goods_list = [
            ['凤爪', 50],
            ['肠粉', 20],
            ['macbook pro', 10000],
            ['肥仔快乐水', 5]
        ]

        for index,goods in enumerate(goods_list):
            print(index,goods)

        choose_num = input('请输入商品编号：').strip()

        if not choose_num.isdigit():
            print('请输入数字')
            continue

        choose_num = int(choose_num)


        if choose_num >=0 and choose_num < len(goods_list):

            good,price = goods_list[choose_num]

            if user_balance >= price:

                if good in shopping_cars:

                    shopping_cars[good] += 1
                else:
                    shopping_cars[good] = 1

                cost += price

                sure = input('确认购买？ 请输入 y/n:').strip()

                if sure == 'y':
                    flag,msg = shopping_interface.pay_interface(user_info['name'],cost)

                    if flag:
                        print(msg)
                        break
                elif sure == 'n':

                    msg = shopping_interface.save_shop_car_interface(user_info['name'],shopping_cars)

                    print(msg)
                    break
            else:
                print('余额不足')

        else:
            print('请输入商品编号！')



@common.login_auth
def check_shopping_car():
    shop_car_s = shopping_interface.check_shop_car_interface(user_info['name'])
    print(shop_car_s)


@common.login_auth
def logout():
    user_info['name'] = None


func_dic = {'1': register,
            '2': login,
            '3': check_balance,
            '4': withdraw,
            '5': transfer,
            '6': repay,
            '7': check_flow,
            '8': shopping_car,
            '9': check_shopping_car,
            '10': logout}


def run():
    while True:
        print('''
         1.注册
         2.登录
         3.查看余额
         4.提现
         5.转账
         6.还款
         7.查看流水
         8.购物车功能
         9.查看购物车
         10.注销
         q.退出
        ''')

        choose = input('请输入功能编号:').strip()

        if choose == 'q':
            break

        if choose not in func_dic:
            print('请选择功能的编号!')
            continue

        func_dic[choose]()
