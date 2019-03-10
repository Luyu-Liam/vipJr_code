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

        # 设置一个输入列表变量
        self.inputList = []
        self.midstr = ''

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
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[0]))
        # relief属性用来设置按钮的样式，取值可以有：FLAT， RAISED, SUNKEN, GROOVE, RIDGE
        self.NumButton.place(x=30, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[1],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[1]))
        self.NumButton.place(x=110, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[2],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[2]))
        self.NumButton.place(x=190, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EE6A50', text=self.ButtonList[3],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[3]))
        self.NumButton.place(x=270, y=80, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[4],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[4]))
        self.NumButton.place(x=30, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[5],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[5]))
        self.NumButton.place(x=110, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[6],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[6]))
        self.NumButton.place(x=190, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[7],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[7]))
        self.NumButton.place(x=270, y=140, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[8],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[8]))
        self.NumButton.place(x=30, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[9],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[9]))
        self.NumButton.place(x=110, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[10],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[10]))
        self.NumButton.place(x=190, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[11],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[11]))
        self.NumButton.place(x=270, y=200, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[12],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[12]))
        self.NumButton.place(x=30, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[13],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[13]))
        self.NumButton.place(x=110, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[14],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[14]))
        self.NumButton.place(x=190, y=260, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#CDBA96', text=self.ButtonList[15],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[15]))
        self.NumButton.place(x=30, y=320, width=150, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#EECFA1', text=self.ButtonList[16],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[16]))
        self.NumButton.place(x=190, y=320, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#E0EEE0', text=self.ButtonList[17],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[17]))
        self.NumButton.place(x=270, y=260, width=70, height=175)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[18],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[18]))
        self.NumButton.place(x=30, y=380, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[19],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[19]))
        self.NumButton.place(x=110, y=380, width=70, height=55)
        self.NumButton = tkinter.Button(master=self.tk, relief=GROOVE, bg='#BFEFFF', text=self.ButtonList[20],
                                        font=self.ButtonFont, command=lambda: self.addButton(self.ButtonList[20]))
        self.NumButton.place(x=190, y=380, width=70, height=55)

    def clear(self):
        self.inputList = []
        self.midstr = ''
        self.count.set(0)

    def checkList(self):
        """
        功能：检查输入列表中是否存在符号，返回最后一个符号的位置，并且对该符号之后的数字部分转换为整数
        :return: 符号位置，最后一部分整数
        """
        result = 0
        locate = -1
        listSum = 0
        for length in range(len(self.inputList)):
            if re.findall(r'[-+*/]', str(self.inputList[length])):
                result = 1
                if length > locate:
                    locate = length

        if result == 1:
            for i in range(locate+1, len(self.inputList)):
                listSum += self.inputList[i] * 10 ** (len(self.inputList) - i - 1)
        else:
            for i in range(len(self.inputList)):
                listSum += self.inputList[i] * 10 ** (len(self.inputList) - i - 1)
        return listSum, locate

    def addButton(self, button):
        if button == self.ButtonList[18]:  # 1/x
            listSum, locate = self.checkList()  # 首先检查一下是否含有符号
            if locate == -1:  # 不含符号，纯数字，那么直接运算即可
                self.inputList = [str(round(eval('1/' + str(listSum)), 5))]
            else:  # 含有符号
                for k in range(locate + 1, len(self.inputList)):
                    del self.inputList[k]
                self.inputList.append(str(round(eval('1/' + str(listSum)), 5)))
        elif button == self.ButtonList[19]:  # %
            pass
        elif button == self.ButtonList[20]:  # sqrt开平方
            pass
        else:
            self.inputList.append(button)
        self.count.set(self.inputList)

    def start(self):
        self.tk.mainloop()


if __name__ == '__main__':
    calc = Calculator()
    calc.start()
