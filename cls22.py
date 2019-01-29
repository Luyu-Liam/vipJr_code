# !/usr/bin/python
# coding: utf8
# Time: 2019-01-27 14:43
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm


# 上节课的作业
class Student:
    def __init__(self, name):
        self.name = name  # 学生姓名
        self.__history = None  # 该学生的历史成绩，默认为空
        self.__math = None  # 该学生的数学成绩，默认为空

    # 设置历史成绩
    def setHistory(self, score):
        self.__history = score

    # 设置数学成绩
    def setMath(self, score):
        self.__math = score

    # 获取历史成绩
    def getHistory(self):
        return self.__history

    # 获取数学成绩
    def getMath(self):
        return self.__math

    # 秀一下自己
    def show(self):
        print("我叫{}, 我的数学成绩是: {}，我的历史成绩是: {}. ".format(self.name, self.__math, self.__history))


if __name__ == '__main__':
    zhangsan = Student("张三")  # 创建学生对象
    # zhangsan.show()
    zhangsan.setHistory(99)
    zhangsan.setMath(14)
    zhangsan.show()


# 这节课的内容：继承性，多态性
# 1. 继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("我是人，我的名字是{}, 年龄是{}。".format(self.name, self.age))

    def talk(self):
        print("我是人类，我会说话")


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def show(self):
        print("我是学生，我的名字是{}，我的分数是{}。".format(self.name, self.score))

    def writePaper(self):
        print('我是学生，我会考试, 一不小心就考了一百分。。。')


#################################################################################


class Animal:
    def run(self):
        print('动物用肢体跑起来')


class Dog(Animal):
    def run(self):
        print('用四只狗爪子跑起来')


class Person(Animal):
    def run(self):
        print("用两只脚跑起来")


# 过去了一千五百年，诞生了一种新的动物：snake
class Snake(Animal):
    def run(self):
        print('用鳞片滑行')


# 编写一个可以让动物们动起来的函数
def moving(cls):
    cls.run()


if __name__ == '__main__':
    moving(Animal())
    moving(Dog())
    moving(Person())





