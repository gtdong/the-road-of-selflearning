'''
用来处理数据
'''


import os
import json
from conf import settings


# 保存数据
def save(user_dic):
    # 判断db文件夹是否存在，若不存在则创建
    if not os.path.exists(settings.DB_PATH):
        os.mkdir(settings.DB_PATH)


    # ATM/db目录/用户名.json
    user_file = '%s/%s.json' % (settings.DB_PATH, user_dic['name'])

    # 写入用户信息
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
        f.flush()



# 查看用户数据
def select(user):  # tank

    db_path = settings.DB_PATH
    user_path = '%s/%s.json' % (db_path, user)  # database/tank.json

    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic

