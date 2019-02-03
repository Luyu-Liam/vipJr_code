# !/usr/bin/python
# coding: utf8
# Time: 2019-01-27 07:55
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

# 字符串转换为数字
a = '123'
b = int(a)
# print(b, type(b))

# 字符串的首字母大写
a = "liam"
b = a.capitalize()
# print(b, a)

# 所有的字母都变为小写
a = "Liam, you are my destiny."
# print(a.lower())

# 设置宽度，并将内容居中
# print(a.center(50, "*"))
# print(a.ljust(50, "*"))
# print(a.rjust(50, '*'))

# 统计字符出现的次数
# print(a.count('a'))

# 判断开头/结尾
# print(a.endswith("."))
# print(a.startswith('a'))

# 寻找子串
# print(a.find('destiny'))

# 字符串的分割
a = "今天是个好日子"
# print("   ".join(a))

# 课后习题
print("Hello\n"*1000)
s = "我是剑士，你好py大法"
print(s[-2:])
print(s[-5:1:-4])


