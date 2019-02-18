# !/usr/bin/python
# coding: utf8
# Time: 2019-01-18 17:06
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm


# 如果不用面向对象，则描述一个事物和对应的动作将会是怎样的？

# 狗的属性
'''
dog1 = {
    "name": '老王',
    "gender": "母",
    "type": "藏獒"
}

dog2 = {
    "name": '旺财',
    "gender": "母",
    "type": "腊肠"
}

person1 = {
    "name": 'xxx',
    "gender": "母",
    "type": "班主任"
}


# 狗的动作
def jiao(dog):
    print("一条狗[{}]，汪汪汪".format(dog['type']))


def chi_shi(dog):
    print("一条狗[{}], 正在吃屎".format(dog['name']))


jiao(person1)
'''


# 把狗的属性和动作都放进函数里面去
def DOG(name, gender, type):
    # 狗的动作
    def jiao():
        print("一条狗[{}]，汪汪汪".format(dog1['type']))

    def chi_shi():
        print("一条狗[{}], 正在吃屎".format(dog1['name']))

    dog1 = {
        "name": name,
        "gender": gender,
        "type": type,
        "jiao": jiao,
        "chi_shi": chi_shi
    }

    return dog1


dg1 = DOG("旺财", "母", "中华田园犬")
dg2 = DOG("老王", "母", "藏獒")
dg1['jiao']()
dg2['chi_shi']()


# 定义一个月饼类
class MoonCake:
    # 如果在设置属性的时候不写self会怎样呢？
    count = 0

    # 构造函数，该函数在对象被创建出来的时候调用.
    def __init__(self, size, color):
        MoonCake.count += 1  # 没有加self，则该属性归类所有，加了self，该属性归对象所有
        self.__size = size  # 属性，表示月饼的大小
        self.__color = color  # 属性，表示月饼的颜色
        self.__secret = "独门秘方"  # 属性一般不希望用户直接访问, 一般通过set，get方法进行设置/获取属性值

    # 方法(函数)
    def eat(self):
        print('我是月饼，来吃我呀')

    def show(self):
        print("我是" + self.__color + "的月饼, 大小为" + str(self.__size))

    def setSecret(self, secret):
        self.__secret = secret

    def getSecret(self, id="no"):
        if id == "内部人":
            return self.__secret
        else:
            return "你是谁？报上名来，饶你不死"

    def setSize(self, size):
        self.__size = size

    def getSize(self):
        return self.__size

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color


if __name__ == '__main__':
    cake = MoonCake(5, 'red')
    cake.show()

    print(cake.getSecret("美国人"))
