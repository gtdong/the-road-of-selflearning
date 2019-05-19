#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
import logging.config
from conf import settings
import os
import shelve

shelve_log = os.path.join(settings.SHEVLE_PATH, 'win.shv')


def save_record(msg):  # 用log往log文件夹下的record.log记录竞猜记录
    log1 = get_logger('lottery')
    log1.critical(msg)


def get_logger(name):  # 根据name提供logger
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger1 = logging.getLogger(name)
    return logger1


def save_win(msg):  # 用shevle模块存放中奖信息到db下的win.shv文件
    if not os.path.exists(shelve_log):
        with shelve.open(shelve_log, writeback=True) as shv_tool:
            shv_tool['info'] = []
            shv_tool['info'].append(msg)
    else:
        with shelve.open(shelve_log, writeback=True) as shv_tool:
            shv_tool['info'].append(msg)
