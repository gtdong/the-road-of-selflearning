# time模块
import time
# 时间戳
res = time.time()  # ***
print(res, type(res))

# time.sleep(1)  # ***
# print(123)

# 自定义延迟
# old_time = time.time()
# while time.time() - old_time < 3:
#     pass
# print(123)

# res = time.localtime()
# print(res.tm_year, type(res))

# ***
# res = time.strftime('%Y-%m-%d %H:%M:%S')
# print(res, type(res))

# time_tuple = (2010, 4, 27, 18, 10, 59, 0, 0, 0)
# res = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
# res = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1556359559))
# print(res)

# print(time.gmtime())

# import calendar
# # 判断闰年
# print(calendar.isleap(2000))
# # 查看某年某月日历
# print(calendar.month(2008, 8))
# # 查看某年某月起始星期与当月天数
# print(calendar.monthrange(2019, 4))
# # 查看某年某月某日是星期几
# print(calendar.weekday(2019, 4, 1))

import datetime
# 当前时间 ***
res = datetime.datetime.now()
print(res, type(res))

# 可以完成时间的运算
print(datetime.datetime.now() + datetime.timedelta(hours=1))

time_obj = datetime.datetime.now()
print(time_obj)

# 修改时间
new_time = time_obj.replace(year=2000, day=1)
print(new_time)

# 格式化时间戳: 2019-04-27
print(datetime.date.fromtimestamp(1556359520))

