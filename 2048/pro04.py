# !/usr/bin/python
# coding: utf8
# Time: 2019-02-16 12:29
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

import curses
"""
try:
    myScreen = curses.initscr()   # 初始化屏幕
    myScreen.addstr("这是一个测试案例")  # 往屏幕上添加字符串
    myScreen.refresh()  # 刷新字符串
    myScreen.getch()  # 等待输入，让我们可以看到结果
finally:
    curses.endwin()  # 恢复终端窗口
"""

try:
    myScreen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    myScreen.clear()
    myScreen.addstr(1, 1, "This is a test", curses.color_pair(1))
    # myScreen.addstr(4, 1, "This is a test", curses.color_pair(2))
    # myScreen.addstr(5, 3, "This is a test", curses.color_pair(3))
    myScreen.refresh()
    myScreen.getch()
finally:
    curses.endwin()
