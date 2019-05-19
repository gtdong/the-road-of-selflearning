LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'o_fmt1': {
            'format': '%(asctime)s:%(levelname)s 【%(name)s】- %(msg)s'
        },
        'o_fmt2': {
            'format': '%(asctime)s:%(levelname)s  - %(msg)s'
        }
    },
    'filters': {},
    'handlers': {
        'o_hd_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',  # 打印到控制台
            'formatter': 'o_fmt1',
            'filename': 'log/sys.log',
            'encoding': 'utf-8',
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,
        },
        'o_hd_cmd': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到控制台
            'formatter': 'o_fmt2'
        }
    },
    'loggers': {
        'o_owen': {
            'level': 'DEBUG',
            'handlers': ['o_hd_file', 'o_hd_cmd']
        },
        'o_zero': {
            'level': 'DEBUG',
            'handlers': ['o_hd_cmd'],
            # 'propagate': True  # 向上传递
        }
    }
}