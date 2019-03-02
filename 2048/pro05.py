# !/usr/bin/python
# coding: utf8
# Time: 2019/3/2 14:26
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import curses
import random
from itertools import chain


# 前面写过的网格类
class Grid(object):
    def __init__(self, size):
        self.size = size
        self.cells = None
        self.score = 0
        self.reset()

    def reset(self):
        self.cells = [[0 for i in range(self.size)] for j in range(self.size)]  # 生成一个size x size大小的零矩阵
        self.add_random_item()
        self.add_random_item()

    def add_random_item(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0]
        (i, j) = random.choice(empty_cells)
        # 90%的概率生成4，10%的概率生成2
        self.cells[i][j] = 4 if random.randrange(100) >= 90 else 2
        full_cells = [self.cells[i][j] for i in range(self.size) for j in range(self.size) if self.cells[i][j] != 0]
        self.score = sum(full_cells)

    def transpose(self):
        self.cells = [list(row) for row in zip(*self.cells)]

    def invert(self):
        self.cells = [row[::-1] for row in self.cells]

    def move_row_left(self, row):
        def tighten(row):
            new_row = [i for i in row if i != 0]
            new_row += [0 for _ in range(len(row) - len(new_row))]
            return new_row

        def merge(row):
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    new_row.append(2*row[i])
                    pair = False

                else:
                    if i+1 < len(row) and row[i] == row[i+1]:
                        new_row.append(0)
                        pair = True
                    else:
                        new_row.append(row[i])
            return new_row

        return tighten(merge(tighten(row)))

    def move_left(self):
        self.cells = [self.move_row_left(row) for row in self.cells]

    def move_right(self):
        self.invert()
        self.move_left()
        self.invert()

    def move_up(self):
        self.transpose()
        self.move_left()
        self.transpose()

    def move_down(self):
        self.transpose()
        self.move_right()
        self.transpose()

    def show_cells(self):
        for row in self.cells:
            print(row)
        print("*"*44)

    def row_can_move_left(self, row):
        def change(i):
            if row[i] == 0 and row[i+1] != 0:
                return True
            if row[i] != 0 and row[i+1] == row[i]:
                return True
        return any(change(i) for i in range(len(row) - 1))

    def can_move_left(self):
        return any(self.row_can_move_left(row) for row in self.cells)

    def can_move_right(self):
        self.invert()
        can = self.can_move_left()
        self.invert()
        return can

    def can_move_up(self):
        self.transpose()
        can = self.can_move_left()
        self.transpose()
        return can

    def can_move_down(self):
        self.transpose()
        can = self.can_move_right()
        self.transpose()
        return can


# 前面写过的屏幕类
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


# 根据前面写的内容，改造成动作指令类
class Action(object):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    RESTART = 'restart'
    EXIT = 'exit'
    actions = [UP, LEFT, DOWN, RIGHT, RESTART, EXIT]
    letter_codes = [ord(ch) for ch in "WASDRQwasdrq"]
    actions_dict = dict(zip(letter_codes, actions * 2))

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def get(self):
        char_ = 'N'
        while char_ not in self.actions_dict:
            char_ = self.stdscr.getch()
        return self.actions_dict[char_]


# 游戏管理类
class GameManager(object):
    def __init__(self, size=4, win_num=2048):  # 默认尺寸为4，默认的胜利分数为2048
        self.size = size
        self.win_num = win_num
        self.reset()

    # 重置
    def reset(self):
        self.state = 'init'
        self.win = False
        self.over = False
        self.score = 0
        self.grid = Grid(self.size)
        self.grid.reset()

    # 创建屏幕对象
    @property
    def screen(self):
        return Screen(screen=self.stdscr, score=self.score, grid=self.grid, win=self.win, over=self.over)

    # 初始化状态
    def state_init(self):
        self.reset()
        return 'game'

    # 游戏状态跳转
    def state_game(self):
        self.screen.draw()
        action = self.action.get()
        if action == Action.RESTART:
            return 'init'
        elif action == Action.EXIT:
            return 'exit'
        if self.move(action):
            if self.is_win:
                return 'win'
            if self.is_over:
                return 'over'
        return 'game'

    # 退出状态
    def state_exit(self):
        self.screen.draw()
        return 'exit'

    # 胜利状态
    def state_win(self):
        self.screen.draw()
        return 'win'

    # 游戏结束状态
    def state_over(self):
        self.screen.draw()
        return 'over'

    # 移动
    def move(self, direction):
        if self.can_move(direction):
            getattr(self.grid, 'move_' + direction)()
            self.grid.add_random_item()
            return True
        else:
            return False

    # 判断是否可以移动，这里需要调用网格类中的方法进行判断
    def can_move(self, direction):
        print(direction)
        try:
            return getattr(self.grid, 'can_move_' + direction)()
        except AttributeError:
            return False

    @property
    def is_win(self):
        return max(chain(*self.grid.cells)) >= self.win_num

    @property
    def is_over(self):
        return not any(self.can_move(move) for move in self.action.actions)

    # 让实例对象变为可调用对象
    def __call__(self, stdscr):
        curses.start_color()
        self.stdscr = stdscr
        self.action = Action(stdscr)
        while self.state != 'exit':
            self.state = getattr(self, 'state_' + self.state)()


if __name__ == '__main__':
    curses.wrapper(GameManager())





