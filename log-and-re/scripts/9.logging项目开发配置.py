# 1.将打印者，句柄，与格式封装成配置信息
# 2.加载配置信息
# 3.使用自定义logger，采用的就是配置信息设置的logger

# 优势：1，2两步是一劳永逸的，后期开发只需要在要记录日志的文件中使用自定义logger



# 一、配置
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'o_fmt1': {
            'format': '%(asctime)s 【%(name)s】- %(msg)s'
        },
        'o_fmt2': {
            'format': '%(asctime)s - %(msg)s'
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

# 二、加载配置
import logging.config
logging.config.dictConfig(LOGGING_DIC)


# 三、使用
log = logging.getLogger('o_zero')
log.critical('信息')

log1 = logging.getLogger('o_owen')
log1.critical('信息')


