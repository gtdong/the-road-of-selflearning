#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from conf import settings
from lib.common import get_logger, save_win, save_record
import random


# 提示用户选择玩法：0退出 1猜大小 2匹配三 3匹配五 其他输入错误，重输
def guess_big():
    guess_dic = {'0': '大', '1': '小'}
    while True:
        result = str(random.randint(0, 1))
        choice = input('''
        0:大，
        1:小
        猜大小，请输入编号(q退出):''').strip()
        if choice == 'q':
            break
        if choice in guess_dic:
            print('您选择了%s' % guess_dic[choice])
            if choice == result:
                print('\033[32;0m 猜对了，结果是%s\033[0m' % guess_dic[result])
                msg = '选择了%s,猜对了' % guess_dic[result]
                save_record(msg)
                save_win(msg)
            else:
                print('\033[31;0m猜错了，结果是%s\033[0m' % guess_dic[result])
                msg = '选择了%s,猜错了' % guess_dic[result]
                save_record(msg)
                save_win(msg)
        else:
            print('输入错误，退出')
            break


def match_three():
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    prize_dic = {
        '1': '三等奖',
        '2': '二等奖',
        '3': '一等奖',
        '0': '没中奖'
    }
    while True:
        count = 0
        list_result = random.sample(l1, k=3)
        choice = input('请输入3个10以内的数字(q退出):').strip()
        if choice == 'q':
            break
        if choice.isdigit():
            for n in list(choice):
                if int(n) in list_result:
                    count += 1
            print(prize_dic[str(count)])
            msg = '您选择了%s,%s,%s,%s' % (
                choice[0], choice[1], choice[2], prize_dic[str(count)])
            save_record(msg)
            save_win(msg)
        else:
            print('请重新输入')
            break


def match_five():
    l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    prize_dic = {
        '1': '五等奖',
        '2': '四等奖',
        '3': '三等奖',
        '4': '二等奖',
        '5': '一等奖',
        '0': '没中奖'
    }
    while True:
        count = 0
        list_result = random.sample(l1, k=5)
        choice = input('请输入5个10以内的数字(q退出):')
        if choice == 'q':
            break
        if choice.isdigit():
            for n in list(choice):
                if int(n) in list_result:
                    count += 1
            print(prize_dic[str(count)])
            msg = '您选择了%s,%s,%s,%s,%s,%s' % (
                choice[0], choice[1], choice[2], choice[3], choice[4], prize_dic[str(count)])
            save_record(msg)
            save_win(msg)
        else:
            print('请重新输入')
            break


func_dic = {
    '1': guess_big,
    '2': match_three,
    '3': match_five
}


def run():
    while True:
        print('''
        q.退出
        1.猜大小
        2.匹配三
        3.匹配五
        ''')
        choose = input('请选择功能编号(q退出)：').strip()

        if choose == 'q':
            break

        if choose not in func_dic:
            print('输入错误，请重新输入')
            continue

        func_dic[choose]()
