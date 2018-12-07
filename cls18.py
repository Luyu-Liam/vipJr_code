# !/usr/bin/python
# coding: utf8
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm


# with open('temp/text.txt', 'r') as f1, open('temp/newtext.txt', 'w+') as f2:
#     for i in f1:
#         f2.write(i)
#     f2.seek(0)
#     print(f2.read())

with open('temp/music.txt', 'rb+') as f1, open('temp/demon.txt', 'ab+') as f2:
    f2.write(f1.read(3))
    f1.seek(0)
    f2.write(f1.read(3))
    f1.seek(12, 0)
    f2.write(f1.read(3))
    f1.seek(-3, 1)
    f2.write(f1.read(3))
    f2.write(f1.read(3))
    f1.seek(-3, 1)
    f2.write(f1.read(3))
    f1.seek(12, 0)
    f2.write(f1.read(3))

