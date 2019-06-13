#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
import pickle
import os
from conf import settings

def save(obj):
    path_obj = os.path.join(settings.BASE_DB,obj.__class__.__name__.lower())
    if not os.path.isdir(path_obj):
        os.mkdir(path_obj)
    path_file = os.path.join(path_obj,obj.name)
    with open(path_file,'wb') as f:
        pickle.dump(obj,f)
        f.flush()

def select(name,type):
    path_obj=os.path.join(settings.BASE_DB,type)
    # print(type)
    if not os.path.isdir(path_obj):
        os.mkdir(path_obj)
    path_file = os.path.join(path_obj,name)
    if os.path.exists(path_file):
        with open(path_file,'rb') as f:
            return pickle.load(f)
    else:
        return False

