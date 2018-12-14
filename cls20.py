# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm
import time


# t0 = time.perf_counter()
# t1 = time.process_time()
# sum = 0
# for i in range(900000):
#     sum += i
# print('cost:', time.perf_counter()-t0)
# print('cost:', time.process_time()-t1)

# print(time.asctime())
# time.sleep(5)
# print(time.asctime())

"""计算2000年4月1日到2018年4月1日一共有多少个闰年，如果是闰年的话把父亲节
   的日期打印出来。（父亲节是每年六月的第三个星期日）
"""
import calendar
number_of_leap = calendar.leapdays(2000, 2018)
print(number_of_leap)
for year in range(2000, 2019):
    if calendar.isleap(year):
        times = 1
        day = 0
        while day < 30 and times < 4:
            day += 1
            if calendar.weekday(year, 6, day) == 6:
                times += 1
        weekday1, _ = calendar.monthrange(year, 1)
        print("The Father's day of {} is : {}.6.{}".format(year, year, day))
        print("The firstday of January is Week {}.".format(weekday1+1))


"""课外兴趣拓展：进度条小程序"""
# scale = 50
#
# print("执行开始".center(scale,"-"))
#
# start = time.perf_counter()
# for i in range(scale+1):
#     a = '*' * i             # i 个长度的 * 符号
#     b = '.' * (scale-i)  # (scale-i) 个长度的 . 符号。符号 * 和 . 总长度为50
#     c = (i/scale)*100  # 显示当前进度，百分之多少
#     dur = time.perf_counter() - start    # 计时，计算进度条走到某一百分比的用时
#
#     # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；
#     # {:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；
#     # {}，对应输出的数为a；{}，对应输出的数为b；
#     # {:.2f}，输出有两位小数的浮点数，对应输出的数为dur；
#     # end=''，用来保证不换行，不加这句默认换行。
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
#
#     time.sleep(0.2)     # 在输出下一个百分之几的进度前，停止0.1秒
# print("\n"+"执行结果".center(scale,'-'))




