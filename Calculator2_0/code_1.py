# !/usr/bin/python
# coding: utf8
# Time: 2019/2/24 16:09
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tkinter
import os
import tkinter.font as tkfont
from tkinter import *


class Calculator(object):
    def __init__(self):
        """1. 开始一个窗口"""
        self.tk = tkinter.Tk()  # 实例化
        self.tk.title("计算器")
        self.tk.minsize(370, 460)
        self.tk.maxsize(400, 400)
        self.tk.resizable(0, 0)  # 禁止调节大小
        self.tk.iconbitmap(os.getcwd() + "/favicon.ico")

        self.ButtonList = [
            '清空', '/', '*', '退格', 7, 8, 9, '-', 4, 5, 6, '+', 1, 2, 3, 0,
            '.', '=', '1/x', '%', 'sqrt']

        """2. 面板显示"""
        # 字体设置
        self.EntryFont = tkfont.Font(self.tk, size=13)
        self.ButtonFont = tkfont.Font(self.tk, size=12)
        # 面板显示
        self.count = tkinter.StringVar()
        self.count.set("0")
        self.label = tkinter.Label(self.tk, bg='#EEE9E9', bd='3', fg='black', anchor='e',
                                   font=self.EntryFont, textvariable=self.count)
        # anchor用来定位内容在面板中的位置，取值为：center, e, w, s, n
        self.label.place(x=30, y=10, width=310, height=40)

        """3. 按钮、输入框设置"""
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[0],
                                        font=self.ButtonFont)
        # relief属性用来设置按钮的样式，取值可以有：FLAT， RAISED, SUNKEN, GROOVE, RIDGE
        self.NumButton.place(x=30, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[1],
                                        font=self.ButtonFont)
        self.NumButton.place(x=110, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[2],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[3],
                                        font=self.ButtonFont)
        self.NumButton.place(x=270, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[4],
                                        font=self.ButtonFont)
        self.NumButton.place(x=30, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[5],
                                        font=self.ButtonFont)
        self.NumButton.place(x=110, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[6],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[7],
                                        font=self.ButtonFont)
        self.NumButton.place(x=270, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[8],
                                        font=self.ButtonFont)
        self.NumButton.place(x=30, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[9],
                                        font=self.ButtonFont)
        self.NumButton.place(x=110, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[10],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[11],
                                        font=self.ButtonFont)
        self.NumButton.place(x=270, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[12],
                                        font=self.ButtonFont)
        self.NumButton.place(x=30, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[13],
                                        font=self.ButtonFont)
        self.NumButton.place(x=110, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[14],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[15],
                                        font=self.ButtonFont)
        self.NumButton.place(x=30, y=320, width=150, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EECFA1', text=self.ButtonList[16],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=320, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#E0EEE0', text=self.ButtonList[17],
                                        font=self.ButtonFont)
        self.NumButton.place(x=270, y=260, width=70, height=175)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[18],
                                        font=self.ButtonFont)
        self.NumButton.place(x=30, y=380, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[19],
                                        font=self.ButtonFont)
        self.NumButton.place(x=110, y=380, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[20],
                                        font=self.ButtonFont)
        self.NumButton.place(x=190, y=380, width=70, height=55)

    def start(self):
        self.tk.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.start()
