#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
def login_auth(func):

    from core import src

    def inner(*args, **kwargs):

        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            src.login()

    return inner
