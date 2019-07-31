#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author Michaeldong
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_PATH = os.path.join(BASE_DIR, 'log')
lottery_log_path = os.path.join(LOG_PATH, 'record.log')
SHEVLE_PATH = os.path.join(BASE_DIR, 'database')

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGING_DIC = {
                  'version': 1,
                  'disable_existing_loggers': False,
                  'formatters': {
                      'o_fmt1': {
                          'format': '%(asctime)s 【%(name)s】- %(msg)s'
                      },
                  },
                  'filters': {},
                  'handlers': {
                      'o_hd_file': {
                          'level': 'WARNING',
                          'class': 'logging.handlers.RotatingFileHandler',  # 打印到控制台
                          'formatter': 'o_fmt1',
                          'filename': lottery_log_path,
                      'encoding': 'utf-8',
                      'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
                      'backupCount': 5,
                  },
                  'o_hd_cmd': {
                      'level': 'DEBUG',
                      'class': 'logging.StreamHandler',  # 打印到控制台
                      'formatter': 'o_fmt1'
                  }
              },
              'loggers': {
    'lottery': {
        'level': 'DEBUG',
        'handlers': ['o_hd_file', 'o_hd_cmd'],
        # 'propagate': True,
    }
}
}
