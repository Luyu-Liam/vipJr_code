import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re

"""
VIP下载器
"""


class APP:
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = ' VIP视频破解助手'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)
        self.userurl = tk.StringVar()

        def author():
            tk.messagebox.showinfo(title="作者", message="陆 宇")

        def howtouse():
            tk.messagebox.showinfo(title='使用手册', message='1.找到您需要播放的视频，复制其网址。\n2.将其网址粘贴到下面的文本框中。\n3.选择一个接口，然后点击【播放】。\n4.如不能正常播放，请尝试更换接口或者自定义接口')

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)
        frame_add = tk.Frame(self.root)

        # Menu菜单
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        filemenu = tk.Menu(menu, tearoff=0)
        moviemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='菜单', menu=filemenu)
        menu.add_cascade(label='友情链接', menu=moviemenu)
        filemenu.add_command(label='使用说明', command=howtouse)
        # filemenu.add_command(label='关于作者', command=lambda: webbrowser.open('https://github.com/Luyu-Liam'))
        filemenu.add_command(label='关于作者', command=author)
        filemenu.add_command(label='退出', command=self.root.quit)

        # 各个网站链接
        moviemenu.add_command(label='腾讯视频', command=lambda: webbrowser.open('http://v.qq.com/'))
        moviemenu.add_command(label='搜狐视频', command=lambda: webbrowser.open('http://tv.sohu.com/'))
        moviemenu.add_command(label='芒果TV', command=lambda: webbrowser.open('http://www.mgtv.com/'))
        moviemenu.add_command(label='爱奇艺', command=lambda: webbrowser.open('http://www.iqiyi.com/'))
        moviemenu.add_command(label='PPTV', command=lambda: webbrowser.open('http://www.bilibili.com/'))
        moviemenu.add_command(label='优酷', command=lambda: webbrowser.open('http://www.youku.com/'))
        moviemenu.add_command(label='乐视', command=lambda: webbrowser.open('http://www.le.com/'))
        moviemenu.add_command(label='土豆', command=lambda: webbrowser.open('http://www.tudou.com/'))
        moviemenu.add_command(label='A站', command=lambda: webbrowser.open('http://www.acfun.tv/'))
        moviemenu.add_command(label='B站', command=lambda: webbrowser.open('http://www.bilibili.com/'))

        # 控件内容设置
        group = tk.Label(frame_1, text='请选择一个接口：', padx=10, pady=10, width=10)
        tb1 = tk.Radiobutton(frame_1, text='接口1', variable=self.v, value=1, width=4, height=3)
        tb2 = tk.Radiobutton(frame_1, text='接口2', variable=self.v, value=2, width=4, height=3)
        tb3 = tk.Radiobutton(frame_1, text='接口3', variable=self.v, value=3, width=4, height=3)
        tb4 = tk.Radiobutton(frame_1, text='接口4', variable=self.v, value=4, width=4, height=3)
        tb5 = tk.Radiobutton(frame_1, text='接口5', variable=self.v, value=5, width=4, height=3)
        tb6 = tk.Radiobutton(frame_1, text='接口6', variable=self.v, value=6, width=4, height=3)
        uservip = tk.Radiobutton(frame_add, text='自定义接口', variable=self.v, value=7, width=10, height=3)
        entryuser = tk.Entry(frame_add, textvariable=self.userurl, highlightcolor='Fuchsia', highlightthickness=1, width=35)


        label1 = tk.Label(frame_2, text="请输入视频链接：")
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play = tk.Button(frame_2, text="播放", font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)
        label3 = tk.Label(frame_2, text=" ")
        label_explain = tk.Label(frame_3, fg='red', font=('楷体', 12),
                                 text='\n请勿用于任何商业用途\n')
        label_warning = tk.Label(frame_3, fg='blue', font=('楷体', 12), text='建议：将Chrome内核浏览器设置为默认浏览器\n合法使用，天天开心\n作者：陆 宇')

        # 控件布局
        frame_1.pack()
        frame_add.pack()

        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        tb3.grid(row=0, column=3)
        tb4.grid(row=0, column=4)
        tb5.grid(row=0, column=5)
        tb6.grid(row=0, column=6)
        uservip.grid(row=1, column=0)
        entryuser.grid(row=1, column=1)
        label1.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        label2.grid(row=0, column=2)
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        label3.grid(row=0, column=4)
        label_explain.grid(row=1, column=0)
        label_warning.grid(row=2, column=0)


    def video_play(self):
        # 视频解析网站地址
        port_1 = 'http://api.visaok.net/?url='
        port_2 = 'http://api.xyingyu.com/?url='
        port_3 = 'http://api.greatchina56.com/?url='
        port_4 = 'http://jx.618g.com/?url='
        port_5 = 'http://jx.jfysz.cn/jx.php/?url='
        port_6 = 'http://api.greatchina56.com/?url='

        # 正则表达是判定是否为合法链接
        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            if self.v.get() == 1:
                # 浏览器打开
                webbrowser.open(port_1 + self.url.get())
            elif self.v.get() == 2:
                webbrowser.open(port_2 + self.url.get())

            elif self.v.get() == 3:
                webbrowser.open(port_3 + self.url.get())

            elif self.v.get() == 4:
                webbrowser.open(port_4 + self.url.get())

            elif self.v.get() == 5:
                webbrowser.open(port_5 + self.url.get())

            elif self.v.get() == 6:
                webbrowser.open(port_6 + self.url.get())

            elif self.v.get() == 7:
                webbrowser.open(self.userurl.get() + self.url.get())


        else:
            msgbox.showerror(title='错误', message='视频链接地址无效，请重新输入！')


    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws / 2) - (self.w / 2))
        y = int((hs / 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))


    def loop(self):
        self.root.resizable(False, False)  # 禁止修改窗口大小
        self.center()  # 窗口居中
        self.root.mainloop()


if __name__ == '__main__':
    app = APP()  # 实例化APP对象
    app.loop()  # loop等待用户事件
