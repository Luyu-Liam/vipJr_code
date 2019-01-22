# !/usr/bin/python
# coding: utf8
# Time: 2019-01-22 22:54
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle as t

"""画一张人脸"""

# 开始画之前的准备工作
t.pencolor('red')
t.pensize(3)
t.penup()
t.goto(-150, 100)
t.pendown()

# 画人脸轮廓
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)

# 画左眼睛
t.pencolor('red')
t.penup()
t.goto(-90, 50)
t.pendown()
t.circle(10, 360)

# 画右眼睛
t.pencolor('red')
t.penup()
t.goto(90, 50)
t.pendown()
t.circle(10, 360)

# 画鼻子
t.pencolor('black')
t.penup()
t.goto(-20, -30)
t.pendown()
t.fd(30)
t.rt(90)
t.fd(10)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(10)

# 画嘴巴
t.pencolor('black')
t.penup()
t.goto(10, -100)
t.pendown()
t.fd(40)

# 画完之后的收尾工作
t.penup()
t.mainloop()
