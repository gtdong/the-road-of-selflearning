#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
from lib import common
from conf import settings
import os

def check_all_school():
    base_dir_school = os.path.join(settings.BASE_DB,'school')
    school_list= common.get_all_file(base_dir_school)
    return school_list

