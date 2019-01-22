# !/usr/bin/python
# coding: utf8
# Time: 2019-01-16 19:11
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import tkinter

"""
# 关于tkinter的基本使用
root = tkinter.Tk()
root.title("vipJr打造的专属计算器")   # 设置窗体标题
root.resizable(0, 0)  # 设置窗体大小的可调性，都设置为0表示不可手动调整窗体大小
root.geometry('300x400')  # 设置窗体尺寸，注意，格式为字符串
btn1 = tkinter.Button(root, text='按钮', bg='green')
btn1.place(x=10, y=10, width=50, height=50)
# t1 = tkinter.Entry(root, bg='gold', bd=3, font=('宋体', 30), state='normal')
t1 = tkinter.Text(root, bg='gold', bd=3, font=('宋体', 30), state='normal')
t1.place(x=10, y=250, width=280, height=150)
label1 = tkinter.Label(root, text='文本框', bd=5, bg='green', anchor='e', font=('宋体', 30))
label1.place(x=10, y=310, width=280, height=50)
root.mainloop()


"""
# 计算器的打造
class GUICal:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('vipJr计算器')
        # 界面布局
        self.layout()

        self.root.mainloop()

    # 计算器主界面摆放
    def layout(self):
        # 显示屏
        show_info = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e',)
        show_info.place(x=5, y=20, width=270, height=32)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e')
        show_label.place(x=5, y=58, width=270, height=32)
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
        button_ce = tkinter.Button(self.root, text='CE')
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
        button_remainder = tkinter.Button(self.root, text='//')
        button_remainder.place(x=225, y=205, width=50, height=50)
        # 数字按钮4
        button_4 = tkinter.Button(self.root, text='4')
        button_4.place(x=5, y=260, width=50, height=50)
        # 数字按钮5
        button_5 = tkinter.Button(self.root, text='5')
        button_5.place(x=60, y=260, width=50, height=50)
        # 数字按钮6
        button_6 = tkinter.Button(self.root, text='6')
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
        button_3 = tkinter.Button(self.root, text='3')
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
        button_plus = tkinter.Button(self.root, text='+')
        button_plus.place(x=170, y=370, width=50, height=50)


if __name__ == '__main__':
    c = GUICal()
