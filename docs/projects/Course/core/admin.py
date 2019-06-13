#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from interface import admin_interface, common_interface, school_interface
from lib import common

admin_info = {'name': None}


def admin_register():
    print('--------管理员注册----------')
    while True:
        name = input('请输入用户名：(q to exit)').strip()
        if name == 'q': break

        if admin_info['name']:
            print('已经登录，不能注册！')
            return
        pwd = input('请输入密码:').strip()
        re_pwd = input('请再输入密码:').strip()

        if re_pwd == pwd:
            flag, msg = admin_interface.admin_register(name, pwd)

            if flag:
                print(msg)
                break
            else:
                print(msg)
                continue
        else:
            print('password not equal!')


def admin_login():
    if admin_info['name']:
        print('已登录，不能重复登录')
        return
    print('管理员登录')
    while True:
        name = input('please input name (q to exit)>>:').strip()
        if name == 'q': break
        pwd = input('please input password (q to exit)..:').strip()
        flag, msg = common_interface.login_interface(name, pwd, 'admin')
        if flag:
            admin_info['name'] = name
            print(msg)
            break
        else:
            print(msg)


@common.login_auth(auth_type='admin')
def create_school():
    print('创建学校')
    while True:
        school_name = input('please input school name(q to exit:)').strip()
        if school_name == 'q': break
        school_address = input('please input school address:').strip()

        flag, msg = admin_interface.create_school(admin_info['name'], school_name, school_address)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth(auth_type='admin')
def create_course():
    print('创建课程')
    while True:
        # 创建课程之前先选学校
        school_name_list = school_interface.check_all_school()
        if not school_name_list:
            print('课程为空，创建课程请先创建学校')
            return
        for i, school in enumerate(school_name_list):
            print('%s schoolName: %s' % (i, school))
        choose = input('请选择校区(输入数字：)')
        if choose == 'q': break
        if choose.isdigit():
            choose = int(choose)
            if choose >= 0 and choose < len(school_name_list):
                course_name = input('please input course name:').strip()
                flag, msg = admin_interface.create_course(admin_info['name'], school_name_list[choose], course_name)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入存在的校区')
        else:
            print('must input number')


@common.login_auth(auth_type='admin')
def create_teacher():
    print('创建老师')
    while True:
        teacher_name = input('please input teacher name:').strip()
        if teacher_name == 'q': break
        flag, msg = admin_interface.create_teacher(admin_info['name'], teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


func_dic = {'1': admin_register,
            '2': admin_login,
            '3': create_school,
            '4': create_teacher,
            '5': create_course, }


def admin_view():
    while True:
        print('''
        1: 注册
        2: 登录
        3: 创建学校
        4: 创建讲师
        5: 创建课程
        ''')
        choose = input('请选择功能(q退出)：').strip()

        if choose == 'q':
            break

        if choose not in func_dic:
            print('请输入正确的功能编号：')
            continue

        func_dic[choose]()
