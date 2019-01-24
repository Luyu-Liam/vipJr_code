# !/usr/bin/python
# coding: utf8
# Time: 2019-01-24 23:01
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random

"""
1. 利用上节课编写的矩阵操作，进行矩阵剩余操作的编写；
2. 回顾random库的基本用法：random(), uniform(), randint(), randrange(), choice(), shuffle(), sample(). 
3. 网格类的编写。
"""


class Grid(object):
    def __init__(self, size):
        self.size = size
        self.cells = None
        self.reset()

    # 复位
    def reset(self):
        self.cells = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.add_random_item()
        self.add_random_item()

    def add_random_item(self):
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.cells[i][j] == 0]
        (i, j) = random.choice(empty_cells)
        self.cells[i][j] = 4 if random.randrange(100) >= 90 else 2

    # 转置
    def __transpose(self):
        self.cells = [list(row) for row in zip(*self.cells)]

    # 左移合并
    def __move_row_left(self, row):
        # 矩阵的左移
        def tighten(row):
            new_row = [i for i in row if i != 0]
            new_row += [0 for _ in range(len(row) - len(new_row))]
            return new_row

        # 相邻位置的相同元素合并
        def merge(row):
            pair = False
            new_row = []
            for i in range(len(row)):
                if pair:
                    new_row.append(row[i] * 2)
                    pair = False
                else:
                    if i + 1 < len(row) and row[i] == row[i + 1]:
                        new_row.append(0)
                        pair = True
                    else:
                        new_row.append(row[i])
            return new_row

        return tighten(merge(tighten(row)))

    # 左右翻转
    def __invert(self):
        self.cells = [row[::-1] for row in self.cells]

    # 矩阵的右移合并
    def move_left(self):
        self.cells = [self.__move_row_left(row) for row in self.cells]

    # 矩阵的右移合并
    def move_right(self):
        self.__invert()
        self.move_left()
        self.__invert()

    # 矩阵的上移合并
    def move_up(self):
        self.__transpose()
        self.move_left()
        self.__transpose()

    # 矩阵的下移合并
    def move_down(self):
        self.__transpose()
        self.move_right()
        self.__transpose()

    def show_cells(self):
        for row in self.cells:
            print(row)
        print("*" * 20)


if __name__ == '__main__':
    dog = Grid(4)
    dog.reset()
    dog.show_cells()
    dog.move_down()
    dog.show_cells()




