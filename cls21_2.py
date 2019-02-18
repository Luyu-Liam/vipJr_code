# !/usr/bin/python
# coding: utf8
# Time: 2019-01-31 16:00
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
"""
一、类里面的两种属性：
    1. 静态属性；类和对象都可以访问
    2. 实例属性：必须对象才可以访问，类无法访问
二、类里面的五种方法：
    1. 实例(对象)方法：第一个参数自动为self，必须有对象才能调用
    2. 属性方法：property装饰器的作用：将方法变为属性
    3. 类方法：加上classmethod装饰器就可以转换为类方法，第一个参数会自动为cls，类方法中不能使用对象的属性
    4. 静态方法：加上staticmethod装饰器就可以转换为静态方法，类和对象的属性都不能使用，相当于类的工具包
    5. 普通方法(没有任何意义，不推荐使用)
"""


class Room:
    counter = 0  # 静态属性
    location = "美国旧金山"
    price = 5.9

    def __init__(self, name, lenght, width):
        Room.counter += 1
        self.name = name
        self.length = lenght
        self.width = width
        self.id = Room.counter

    @property  # 加上这个装饰器，方法"变"属性
    def area(self):
        return self.length * self.width

    @classmethod  # 类方法
    def tell_info(cls):
        print("Location:{}, Price:{}个亿/平米".format(cls.location, cls.price))
        # print(self.width)

    @staticmethod  # 静态方法
    def calc_price(price, length, width):
        area = length * width
        result = price * area
        return result

    def test(x, y):  # 不是静态方法，只能通过类调用，不能通过对象调用
        return x + y

    def getAllPrice(self):  # 对象方法(实例方法)
        return Room.calc_price(Room.price, self.length, self.width)


if __name__ == '__main__':
    r1 = Room("厕所", 3, 5)
    r2 = Room('客厅', 5, 8)
    print(r1.getAllPrice())
    print(r2.getAllPrice())
