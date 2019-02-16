# !/usr/bin/python
# coding: utf8
# Time: 2019-02-16 12:29
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import curses
# 1
# 在终端中显示内容的基本操作
"""
try:
    myScreen = curses.initscr()   # 初始化屏幕
    myScreen.addstr("这是一个测试案例")  # 往屏幕上添加字符串
    myScreen.refresh()  # 刷新字符串
    myScreen.getch()  # 等待输入，让我们可以看到结果
finally:
    curses.endwin()  # 恢复终端窗口
"""

# 2
# 如何给终端中的显示添加颜色呢？
"""
try:
    myScreen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    myScreen.clear()
    myScreen.addstr(1, 1, "This is a test", curses.color_pair(1))
    myScreen.addstr(2, 1, "This is a test", curses.color_pair(2))
    myScreen.addstr(3, 1, "This is a test", curses.color_pair(3))
    myScreen.refresh()
    myScreen.getch()
finally:
    curses.endwin()
"""


# 3
# 可以利用wrapper帮我们简化代码
"""
def main(stdscreen):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    stdscreen.clear()
    stdscreen.addstr(1, 1, "This is a test", curses.color_pair(1))
    stdscreen.addstr(2, 1, "This is a test", curses.color_pair(2))
    stdscreen.addstr(3, 1, "This is a test", curses.color_pair(3))
    stdscreen.refresh()
    stdscreen.getch()


curses.wrapper(main)
"""


# 4
# 关于format的补充
# 4.1 通过关键字
# print("隔壁{名字}今天在{动作}".format(名字="老王", 动作="写代码"))

# 4.2 通过字典
# grade = {'name': "Lizzy", "score": 99}
# print("{name}的python课程考了{score}分".format(**grade))

# 4.3 通过位置
# print("{1}的python课程考了{0}分".format(99, "Lizzy"))

# 4.4 填充和对齐
# ^<>分别表示居中、左对齐、右对齐。后面接宽度
# print("{:^10}".format('star'))
# print("{:>10}".format('star'))
# print("{:<10}".format('star'))
# print("{:*<10}".format('star'))
# print("{:&>10}".format('star'))


# 5
# 绘制屏幕类
class Screen(object):
    help_string1 = "(W)up (S)down (A)left (D)right"
    help_string2 = "     (R)Restart (Q)Exit"
    over_string = "           GAME OVER"
    win_string = "          YOU WIN!"

    def __init__(self, screen=None, grid=None, score=0, over=False, win=False):
        self.screen = screen
        self.grid = grid
        self.score = score
        self.over = over
        self.win = win
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # 用颜色渲染字符串，并绘制到屏幕上
    def cast(self, string, colorPair=1):
        self.screen.addstr(string + '\n', curses.color_pair(colorPair))

    # 绘制一行的数字
    def draw_row(self, row):
        self.cast("".join("|{: ^5}".format(num) if num > 0 else "|     " for num in row) + "|", 2)

    def draw(self):
        self.screen.clear()
        self.score = self.grid.score
        self.cast("SCORE: " + str(self.score))  # 显示分数
        for row in self.grid.cells:
            self.cast("+-----"*self.grid.size + "+", 2)   # 绘制分割线
            self.draw_row(row)
        self.cast("+-----"*self.grid.size + "+", 2)

        if self.win:
            self.cast(self.win_string)
        else:
            if self.over:
                self.cast(self.over_string)
            else:
                self.cast(self.help_string1)
        self.cast(self.help_string2)
        self.cast("win:{} over:{}".format(self.win, self.over))


def main(scr):
    curses.start_color()
    g = Grid(4)
    s = Screen(screen=scr, grid=g)
    s.draw()
    scr.getch()


if __name__ == '__main__':
    curses.wrapper(main)



