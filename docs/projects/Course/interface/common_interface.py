#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from db import models


def login_interface(name, pwd, type):
    if type == 'admin':
        obj = models.Admin.get_obj_by_name(name)
    elif type == 'teacher':
        obj = models.Teacher.get_obj_by_name(name)
    elif type == 'student':
        obj = models.Student.get_obj_by_name(name)
    else:
        return False, 'error'
    if obj:
        if pwd == obj.password:
            return True, '%s :%slogin successful' % (type, name)
        else:
            return False, 'password erro'
    else:
        return False, '%s :%s is not exist' % (type, name)
