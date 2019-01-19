# !/usr/bin/python
# coding: utf8
# Time: 2019-01-19 14:48
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

# 复习上节课的zip()函数
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7]

# zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个一个的元组
d1 = zip(a, b)
# print(list(d1))

# 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
d2 = zip(a, c)
# print(list(d2))

matrix = [[1, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]


# 矩阵的转置
def transpose(arr):
    # return list(zip(*arr))  # 可以这样写吗？
    return [list(row) for row in zip(*arr)]   # 想一想，这里的*是什么意思呢？


# 矩阵的左右翻转
def invert(arr):
    return [row[::-1] for row in arr]


# 左移合并
def move_row_left(row):
    # 矩阵的左移
    def tighten(row):
        new_row = [i for i in row if i != 0]
        new_row += [0 for _ in range(len(row)-len(new_row))]
        return new_row

    # 相邻位置的相同元素合并
    def merge(row):
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(row[i]*2)
                pair = False
            else:
                if i+1 < len(row) and row[i] == row[i+1]:
                    new_row.append(0)
                    pair = True
                else:
                    new_row.append(row[i])
        return new_row
    return tighten(merge(tighten(row)))


if __name__ == '__main__':
    print(matrix)
    # print(transpose(matrix))
    # print(invert(matrix))
    # print(tighten(matrix[3]))
    # print(merge(matrix[1]))
    print(move_row_left([0, 0, 1]))




