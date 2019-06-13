#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from core import admin, student, teacher
from interface import common_interface,school_interface,admin_interface

func_dic = {'1': admin.admin_view,
            '2': teacher.teacher_view,
            '3': student.student_view}


def run():
    while True:
        print('''
        1: 管理视图
        2: 讲师视图
        3: 学员视图
        
        ''')

        choose = input('请选择编号（按q退出）：').strip()

        if choose == 'q':
            break

        if choose not in func_dic:
            continue

        func_dic[choose]()
