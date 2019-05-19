
# 登录认证装饰器
def login_auth(func):

    from core import src

    def inner(*args, **kwargs):

        if src.user_info['name']:
            res = func(*args, **kwargs)
            return res
        else:
            src.login()

    return inner


# 日志功能
import logging.config

from conf import settings

''' 在lib文件夹的common文件中生成日志对象 '''
#生成日志对象
def get_logger(name):

    # 先把日志配置传给logging
    logging.config.dictConfig(settings.LOGGING_DIC)

    # 生成日志对象--> 接收的是name， 根据name打印相应的日志
    logger = logging.getLogger(name)

    return logger

# user_logger = get_logger('user')
# user_logger.info('什么什么用户登录了一次!')



