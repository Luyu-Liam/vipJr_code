# !/usr/bin/python
# coding: utf8
# Time: 2019-01-02 19:18
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import curses

"""
语法复习：
1. 列表生成器；
2. zip()函数的使用
"""

if __name__ == '__main__':

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    RESTART = 'restart'
    EXIT = 'exit'
    actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
    letter_codes = [ord(ch) for ch in "WASDRQwasdrq"]
    actions_dict = dict(zip(letter_codes, actions * 2))

    char = 'N'


    def get(scr):
        while True:
            char_ = 'N'
            while char_ not in actions_dict:
                char_ = scr.getch()
            scr.addstr(actions_dict[char_] + " ")


    curses.wrapper(get)
