# !/usr/bin/python
# coding: utf8
# Time: 2019-01-27 07:28
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle as f


color = ["red", 'cyan', 'green', 'blue']
f.speed(10)
f.penup()
f.goto(-200, 200)
f.pendown()
for i in range(3000):
    f.pencolor(color[i%4])
    f.fd(300)
    f.rt(91)

f.mainloop()




