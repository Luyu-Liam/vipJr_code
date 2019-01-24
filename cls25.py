# !/usr/bin/python
# coding: utf8
# Time: 2019-01-23 16:11
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tkinter
import tkinter.messagebox

"""
lambda表达式:
虽说是表达式，其实它是一个函数，匿名函数。
"""

"""
# lambda表达式举例
f1 = lambda x, y, z: x + y + z
# print(f1(2, 3, 4))


f2 = lambda x, y, z: x - y - z
f3 = lambda x, y, z: x * y * z
f4 = lambda x, y, z: x / y / z


# 函数本身也可以作为函数参数进行传递
def deal_with3(x, y, z, f):
    result = f(x, y, z)
    return result


# print(deal_with3(9, 6, 3, f4))

# lambda表达式的第二种用法
L = [(lambda x: x ** 2), (lambda x: x ** 3), (lambda x: x**4)]
print(L[0](2), L[1](2), L[2](2))

D = {'f1': lambda: 2+3,
     'f2': lambda: 2*3,
     'f3': lambda: 2**3}
# print(D['f2'], D['f2'], D['f3'])   # 想一下这样写和下面写有什么不一样？
print(D['f2'](), D['f2'](), D['f3']())
"""


"""计算器功能的完善"""
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

    def clickHandler(self, value):
        self.showInfo.set(cal.record(value))

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
        button_7 = tkinter.Button(self.root, text='7', command=lambda: self.clickHandler('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        # 数字按钮8
        button_8 = tkinter.Button(self.root, text='8', command=lambda: self.clickHandler('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        # 数字按钮9
        button_9 = tkinter.Button(self.root, text='9', command=lambda: self.clickHandler('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        # 功能按钮/
        button_division = tkinter.Button(self.root, text='/', command=lambda: self.clickHandler('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        # 功能按钮%
        button_remainder = tkinter.Button(self.root, text='%', command=lambda: self.clickHandler('%'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        # 数字按钮4
        button_4 = tkinter.Button(self.root, text='4', command=lambda: self.clickHandler('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        # 数字按钮5
        button_5 = tkinter.Button(self.root, text='5', command=lambda: self.clickHandler('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        # 数字按钮6
        button_6 = tkinter.Button(self.root, text='6', command=lambda: self.clickHandler('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        # 功能按钮*
        button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.clickHandler('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        # 功能按钮1/x
        button_reciprocal = tkinter.Button(self.root, text='1/x')
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        # 数字按钮1
        button_1 = tkinter.Button(self.root, text='1', command=lambda: self.clickHandler('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        # 数字按钮2
        button_2 = tkinter.Button(self.root, text='2', command=lambda: self.clickHandler('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        # 数字按钮3
        button_3 = tkinter.Button(self.root, text='3', command=lambda: self.clickHandler('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        # 功能按钮-
        button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.clickHandler('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        # 功能按钮=
        button_equal = tkinter.Button(self.root, text='=', command=lambda: self.showResult.set(self.cal.equal()))
        button_equal.place(x=225, y=315, width=50, height=105)
        # 数字按钮0
        button_0 = tkinter.Button(self.root, text='0', command=lambda: self.clickHandler('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        # 功能按钮.
        button_point = tkinter.Button(self.root, text='.', command=lambda: self.clickHandler('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        # 功能按钮+
        button_plus = tkinter.Button(self.root, text='+', command=lambda: self.clickHandler('+'))
        button_plus.place(x=170, y=370, width=50, height=50)


class Cal:
    def __init__(self):
        self.showText = ''  # 用来显示运算的式子
        self.showResult = ''  # 用来显示运算结果

    def clear(self):
        self.showResult = ""
        self.showText = ""
        return self.showText, self.showResult

    def record(self, t):
        self.showText += t
        return self.showText

    def equal(self):
        self.showResult = self.showText.replace("%", "/100")
        result = eval(self.showResult)
        return result


if __name__ == '__main__':
    cal = Cal()
    c = GUICal(cal)
