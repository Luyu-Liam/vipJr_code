import tkinter
import math
import tkinter.messagebox


class calculator:
    # ���沼�ַ���
    def __init__(self):
        # ���������棬���ұ��浽��Ա������
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('vipJr������')
        # ������ʽ���ı���
        self.result = tkinter.StringVar()
        self.result.set(0)
        # ����һ��ȫ�ֱ���  �������ֺ�f���ŵ��б�
        self.lists = []
        # ���һ�������ж��Ƿ���������ŵı�־
        self.ispresssign = False
        # ���沼��
        self.menus()
        self.layout()
        self.root.mainloop()

    # �������˵�����ڷ�
    def menus(self):
        # ��Ӳ˵�
        # �����ܲ˵�
        allmenu = tkinter.Menu(self.root)
        # ����Ӳ˵�
        filemenu = tkinter.Menu(allmenu, tearoff=0)
        # ���ѡ�
        filemenu.add_command(label='��׼��(T)            Alt+1', command=self.myfunc)
        filemenu.add_command(label='��ѧ��(S)            Alt+2', command=self.myfunc)
        filemenu.add_command(label='����Ա(P)            Alt+3', command=self.myfunc)
        filemenu.add_command(label='ͳ����Ϣ(A)        Alt+4', command=self.myfunc)
        # ��ӷָ���
        filemenu.add_separator()
        # ���ѡ�
        filemenu.add_command(label='��ʷ��¼(Y)      Ctrl+H', command=self.myfunc)
        filemenu.add_command(label='���ַ���(I)', command=self.myfunc)
        # ��ӷָ���
        filemenu.add_separator()
        # ���ѡ�
        filemenu.add_command(label='����(B)             Ctrl+F4', command=self.myfunc)
        filemenu.add_command(label='��λת��(U)      Ctrl+U', command=self.myfunc)
        filemenu.add_command(label='���ڼ���(D)      Ctrl+E', command=self.myfunc)
        menu1 = tkinter.Menu(filemenu, tearoff=0)
        menu1.add_command(label='��Ѻ(M)', command=self.myfunc)
        menu1.add_command(label='��������(V)', command=self.myfunc)
        menu1.add_command(label='�ͺ�(mpg)(F)', command=self.myfunc)
        menu1.add_command(label='�ͺ�(l/100km)(U)', command=self.myfunc)
        filemenu.add_cascade(label='������(W)', menu=menu1)
        allmenu.add_cascade(label='�鿴(V)', menu=filemenu)

        # ����Ӳ˵�2
        editmenu = tkinter.Menu(allmenu, tearoff=0)
        # ���ѡ�
        editmenu.add_command(label='����(C)         Ctrl+C', command=self.myfunc)
        editmenu.add_command(label='ճ��(V)         Ctrl+V', command=self.myfunc)
        # ��ӷָ���
        editmenu.add_separator()
        # ���ѡ�
        menu2 = tkinter.Menu(filemenu, tearoff=0)
        menu2.add_command(label='������ʷ��¼(I)', command=self.myfunc)
        menu2.add_command(label='�༭(E)                      F2', command=self.myfunc)
        menu2.add_command(label='ȡ���༭(N)            Esc', command=self.myfunc)
        menu2.add_command(label='���(L)    Ctrl+Shift+D', command=self.myfunc)
        editmenu.add_cascade(label='��ʷ��¼(H)', menu=menu2)
        allmenu.add_cascade(label='�༭(E)', menu=editmenu)

        # ����Ӳ˵�3
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        # ���ѡ�
        helpmenu.add_command(label='�鿴����(V)       F1', command=self.myfunc)
        # ��ӷָ���
        helpmenu.add_separator()
        # ���ѡ�
        helpmenu.add_command(label='���ڼ�����(A)', command=self.myfunc)
        allmenu.add_cascade(label='����(H)', menu=helpmenu)

        self.root.config(menu=allmenu)

    # ������������ڷ�
    def layout(self):
        # ��ʾ��
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('����', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)
        # ���ܰ�ťMC
        button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
        button_mc.place(x=5, y=95, width=50, height=50)
        # ���ܰ�ťMR
        button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
        button_mr.place(x=60, y=95, width=50, height=50)
        # ���ܰ�ťMS
        button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
        button_ms.place(x=115, y=95, width=50, height=50)
        # ���ܰ�ťM+
        button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
        button_mjia.place(x=170, y=95, width=50, height=50)
        # ���ܰ�ťM-
        button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
        button_mjian.place(x=225, y=95, width=50, height=50)
        # ���ܰ�ť��
        button_zuo = tkinter.Button(self.root, text='��', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)
        # ���ܰ�ťCE
        button_ce = tkinter.Button(self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)
        # ���ܰ�ťC
        button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)
        # ���ܰ�ť��
        button_zf = tkinter.Button(self.root, text='��', command=self.zf)
        button_zf.place(x=170, y=150, width=50, height=50)
        # ���ܰ�ť��
        button_kpf = tkinter.Button(self.root, text='��', command=self.kpf)
        button_kpf.place(x=225, y=150, width=50, height=50)
        # ���ְ�ť7
        button_7 = tkinter.Button(self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        # ���ְ�ť8
        button_8 = tkinter.Button(self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        # ���ְ�ť9
        button_9 = tkinter.Button(self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        # ���ܰ�ť/
        button_division = tkinter.Button(self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        # ���ܰ�ť%
        button_remainder = tkinter.Button(self.root, text='//', command=lambda: self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        # ���ְ�ť4
        button_4 = tkinter.Button(self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        # ���ְ�ť5
        button_5 = tkinter.Button(self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        # ���ְ�ť6
        button_6 = tkinter.Button(self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        # ���ܰ�ť*
        button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        # ���ܰ�ť1/x
        button_reciprocal = tkinter.Button(self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        # ���ְ�ť1
        button_1 = tkinter.Button(self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        # ���ְ�ť2
        button_2 = tkinter.Button(self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        # ���ְ�ť3
        button_3 = tkinter.Button(self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        # ���ܰ�ť-
        button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        # ���ܰ�ť=
        button_equal = tkinter.Button(self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)
        # ���ְ�ť0
        button_0 = tkinter.Button(self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        # ���ܰ�ť.
        button_point = tkinter.Button(self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        # ���ܰ�ť+
        button_plus = tkinter.Button(self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)

    # �������˵�����
    def myfunc(self):
        tkinter.messagebox.showinfo('', '����Ա�����ڵ���ǰ������Ҳ�������Ĺ��ܣ�ֻ��װ�ζ��ѡ�')

    # ���ַ���
    def pressnum(self, num):
        # ȫ�ֻ�����
        # �ж��Ƿ������������
        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
            # ����������ŵ�״̬
            self.ispresssign = False
        if num == '.':
            num = '0.'
        # ��ȡ����е�ԭ������
        oldnum = self.result.get()
        # �жϽ��������Ƿ�Ϊ0
        if oldnum == '0':
            self.result.set(num)
        else:
            # �������°��µ�����
            newnum = oldnum + num

            # �����µ�����д�������
            self.result.set(newnum)

    # ���㺯��
    def presscalculate(self, sign):
        # �����Ѿ����µ����ֺ��������
        # ��ȡ��������
        num = self.result.get()
        self.lists.append(num)
        # ���水�µĲ�������
        self.lists.append(sign)
        # �����������Ϊ����״̬
        self.ispresssign = True

    # ��ȡ������
    def pressequal(self):
        # ��ȡ���е��б��е����ݣ�֮ǰ�����ֺͲ�����
        # ��ȡ��ǰ�����ϵ�����
        curnum = self.result.get()
        # ����ǰ��������ִ����б�
        self.lists.append(curnum)
        # ���б�ת��Ϊ�ַ���
        calculatestr = ''.join(self.lists)
        # ʹ��evalִ���ַ����е����㼴��
        endnum = eval(calculatestr)
        # ����������ʾ�ڽ�����
        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # ��������б�
        self.lists.clear()

    # ��δ����˵��
    def wait(self):
        tkinter.messagebox.showinfo('', '������Ŭ����ʵ�֣����ڴ�2.0�汾�ĸ���')

    # ����������
    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    # ����������
    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)

    # 1/x��������
    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # ��������б�
        self.lists.clear()

    # C��������
    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)

    # �̰�������
    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        # ��������б�
        self.lists.clear()


# ʵ��������
mycalculator = calculator()