import logging

# root打印者，用logging.basicConfig来配置
# logging.critical('12345')

# 1.打印者：自定义的打印者如何配置
log1 = logging.getLogger('Owen')
# log1.critical('67890')

log2 = logging.getLogger('Zero')
# log2.critical('00000')


# 2.输出位置：两个文件输出位置与一个控制台输出位置
hd_a = logging.FileHandler('log/a.log', encoding='utf-8')
hd_b = logging.FileHandler('log/b.log', encoding='utf-8')
hd_cmd = logging.StreamHandler()


# )) 为输出者绑定输出位置
log1.addHandler(hd_a)
log1.addHandler(hd_b)

log2.addHandler(hd_b)
log2.addHandler(hd_cmd)


# 3.输出格式
fmt1 = logging.Formatter('%(asctime)s 【%(name)s】- %(msg)s')
fmt2 = logging.Formatter('%(asctime)s - %(msg)s')


# ))将格式绑定给输出位置(句柄)
hd_a.setFormatter(fmt1)
hd_b.setFormatter(fmt1)
hd_cmd.setFormatter(fmt2)


# 级别控制: 打印者规定打印级别，输出位置(句柄)再可以二次限定，级别>=打印者级别
log2.setLevel(logging.DEBUG)
hd_b.setLevel(logging.WARNING)
hd_cmd.setLevel(logging.DEBUG)

log2.debug('debug msg')
log2.info('info msg')
log2.warning('warning msg')
log2.error('error msg')
log2.critical('critical msg')


# 4.输出
# log1.critical('log1 输出的 critical msg')
# log2.critical('log2 输出的 critical msg')


