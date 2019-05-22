import logging
import sys

# 2.日志的基本配置
logging.basicConfig(
    # 输出级别
    # level=logging.INFO,
    level=10,

    # 输出位置
    # stream=sys.stderr,  # sys.stdout  往控制台输出
    filename='log/my.log',  # 往文件输出  => 如果需要同时往多个位置输出，需要handles

    # 输出格式
    format='%(asctime)s[%(name)s]: %(msg)s',
    datefmt='%H:%M:%S'
)
# print(sys.stdin.readline())

# 1.五大级别
# print('123')
# print(a)
logging.debug('debug msg')
logging.info('info msg')
logging.warning('warning msg')
# logging.warn('warning msg')
logging.error('error msg')
logging.critical('critical msg 哈哈')
logging.fatal('critical msg')

