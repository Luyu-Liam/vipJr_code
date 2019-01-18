# !/usr/bin/python
# coding: utf8
# Time: 2019-01-18 10:24
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tkinter
"""
今天完成功能：
1. 点击按钮，显示框可以显示出输入的文本信息（新增一个输入框）；
2. 处理百分号的问题，计算4+36%的结果（用到eval()函数）；
3. 清楚文本框的功能。

"""


class GUICal:
    def __init__(self, cal):
        self.cal = cal
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('vipJr计算器')
        self.showInfo = tkinter.StringVar()
        self.showInfo.set(self.cal.showText)
        self.showResult = tkinter.StringVar()
        self.showResult.set(self.cal.showResult)
        # 界面布局
        self.layout()
        self.root.mainloop()

    def show3(self):
        self.showInfo.set(self.cal.record('3'))

    def show4(self):
        self.showInfo.set(self.cal.record('4'))

    def show6(self):
        self.showInfo.set(self.cal.record('6'))

    def showpersent(self):
        self.cal.record('%')
        self.showInfo.set(self.cal.persent()[0])
        self.showResult.set(self.cal.persent()[1])

    def showplus(self):
        self.showInfo.set(self.cal.record("+"))

    def clear(self):
        self.showInfo.set(self.cal.clear()[0])
        self.showResult.set(self.cal.clear()[1])

    # 计算器主界面摆放
    def layout(self):
        # 显示屏
        show_info = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e',
                                  textvariable=self.showInfo)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e',
                                   textvariable=self.showResult)
        show_label.place(x=5, y=58, width=270, height=32)
        show_info.place(x=5, y=20, width=270, height=32)
        # 功能按钮MC
        button_mc = tkinter.Button(self.root, text='MC')
        button_mc.place(x=5, y=95, width=50, height=50)
        # 功能按钮MR
        button_mr = tkinter.Button(self.root, text='MR')
        button_mr.place(x=60, y=95, width=50, height=50)
        # 功能按钮MS
        button_ms = tkinter.Button(self.root, text='MS')
        button_ms.place(x=115, y=95, width=50, height=50)
        # 功能按钮M+
        button_mjia = tkinter.Button(self.root, text='M+')
        button_mjia.place(x=170, y=95, width=50, height=50)
        # 功能按钮M-
        button_mjian = tkinter.Button(self.root, text='M-')
        button_mjian.place(x=225, y=95, width=50, height=50)
        # 功能按钮←
        button_zuo = tkinter.Button(self.root, text='←')
        button_zuo.place(x=5, y=150, width=50, height=50)
        # 功能按钮CE
        button_ce = tkinter.Button(self.root, text='CE', command=self.clear)
        button_ce.place(x=60, y=150, width=50, height=50)
        # 功能按钮C
        button_c = tkinter.Button(self.root, text='C')
        button_c.place(x=115, y=150, width=50, height=50)
        # 功能按钮±
        button_zf = tkinter.Button(self.root, text='±')
        button_zf.place(x=170, y=150, width=50, height=50)
        # 功能按钮√
        button_kpf = tkinter.Button(self.root, text='√')
        button_kpf.place(x=225, y=150, width=50, height=50)
        # 数字按钮7
        button_7 = tkinter.Button(self.root, text='7')
        button_7.place(x=5, y=205, width=50, height=50)
        # 数字按钮8
        button_8 = tkinter.Button(self.root, text='8')
        button_8.place(x=60, y=205, width=50, height=50)
        # 数字按钮9
        button_9 = tkinter.Button(self.root, text='9')
        button_9.place(x=115, y=205, width=50, height=50)
        # 功能按钮/
        button_division = tkinter.Button(self.root, text='/')
        button_division.place(x=170, y=205, width=50, height=50)
        # 功能按钮%
        button_remainder = tkinter.Button(self.root, text='%', command=self.showpersent)
        button_remainder.place(x=225, y=205, width=50, height=50)
        # 数字按钮4
        button_4 = tkinter.Button(self.root, text='4', command=self.show4)
        button_4.place(x=5, y=260, width=50, height=50)
        # 数字按钮5
        button_5 = tkinter.Button(self.root, text='5')
        button_5.place(x=60, y=260, width=50, height=50)
        # 数字按钮6
        button_6 = tkinter.Button(self.root, text='6', command=self.show6)
        button_6.place(x=115, y=260, width=50, height=50)
        # 功能按钮*
        button_multiplication = tkinter.Button(self.root, text='*')
        button_multiplication.place(x=170, y=260, width=50, height=50)
        # 功能按钮1/x
        button_reciprocal = tkinter.Button(self.root, text='1/x')
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        # 数字按钮1
        button_1 = tkinter.Button(self.root, text='1')
        button_1.place(x=5, y=315, width=50, height=50)
        # 数字按钮2
        button_2 = tkinter.Button(self.root, text='2')
        button_2.place(x=60, y=315, width=50, height=50)
        # 数字按钮3
        button_3 = tkinter.Button(self.root, text='3', command=self.show3)
        button_3.place(x=115, y=315, width=50, height=50)
        # 功能按钮-
        button_subtraction = tkinter.Button(self.root, text='-')
        button_subtraction.place(x=170, y=315, width=50, height=50)
        # 功能按钮=
        button_equal = tkinter.Button(self.root, text='=')
        button_equal.place(x=225, y=315, width=50, height=105)
        # 数字按钮0
        button_0 = tkinter.Button(self.root, text='0')
        button_0.place(x=5, y=370, width=105, height=50)
        # 功能按钮.
        button_point = tkinter.Button(self.root, text='.')
        button_point.place(x=115, y=370, width=50, height=50)
        # 功能按钮+
        button_plus = tkinter.Button(self.root, text='+', command=self.showplus)
        button_plus.place(x=170, y=370, width=50, height=50)


class Cal:
    def __init__(self):
        self.symbols = ['+', '-', '*', '/']
        self.showText = ''  # 用来显示运算的式子
        self.showResult = ''  # 用来显示运算结果

    def clear(self):
        self.showResult = ""
        self.showText = ""
        return self.showText, self.showResult

    def record(self, t):
        self.showText += t
        return self.showText

    def persent(self):
        self.showResult = self.showText.replace('%', '/100')
        return self.showText, str(eval(self.showResult))


if __name__ == '__main__':
    cal = Cal()
    c = GUICal(cal)
