# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm


import time
ticks = time.time()
print("当前时间戳为：",ticks)

localtime = time.localtime()
print('本地时间为：', localtime)

ltime = time.asctime()
print('本地时间为：', ltime)

print(time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))

print(time.strptime("2018-12-09 16:47:52 Sunday", "%Y-%m-%d %H:%M:%S %A"))

import calendar
cal = calendar.month(2018,12)
print(cal)
for i in range(1, 13):
    print(calendar.month(2018, i))
print(calendar.calendar(2018))

print(calendar.firstweekday())
print(calendar.calendar(2018, w=2, l=1, c=20))
print(calendar.isleap(2018))
print(calendar.month(2018, 12, w=2, l=1))
print(calendar.monthrange(2018, 12))
print(calendar.weekday(2018, 12, 12))

print("当前日期为：", time.strftime("%Y-%m-%d %A", time.localtime()))
