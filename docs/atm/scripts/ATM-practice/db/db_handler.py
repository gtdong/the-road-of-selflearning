#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
import os
import json
from conf import settings



def select(user):
    db_path = settings.DB_PATH
    user_path = '%s/%s.json' % (db_path, user)  # database/tank.json

    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


def save(user_dic):
    if not os.path.exists(settings.DB_PATH):
        os.mkdir(settings.DB_PATH)

    user_file = '%s/%s.json' % (settings.DB_PATH, user_dic['name'])

    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
        f.flush()

