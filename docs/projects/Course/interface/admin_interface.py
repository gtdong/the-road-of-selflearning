#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import models


def admin_register(name, pwd):
    obj = models.Admin.get_obj_by_name(name)
    if not obj:
        admin = models.Admin()
        admin.register(name, pwd)
        return True, 'admin %s register success' % name
    else:
        return False, 'userName exisit,please change'


def create_school(name, school_name, school_address):
    obj = models.School.get_obj_by_name(school_name)
    if not obj:
        admin_obj = models.Admin.get_obj_by_name(name)
        admin_obj.create_school(school_name, school_address)
        return True, 'school create success'
    else:
        return False, 'school already exist'


def create_teacher(admin_name, teacher_name, password='456'):
    obj = models.Teacher.get_obj_by_name(teacher_name)

    if not obj:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_teacher(teacher_name, password)
        return True, 'teacher create successful'
    else:
        return False, 'teacher already exist'


def create_course(admin_name, school_name, course_name):
    course_obj = models.Course.get_obj_by_name(course_name)
    if not course_obj:
        admin_obj = models.Admin.get_obj_by_name(admin_name)
        admin_obj.create_course(course_name)
        school_obj = models.School.get_obj_by_name(school_name)
        school_obj.add_course(course_name)
        return True, 'create course success'
    else:
        return False, 'course has already existed'
