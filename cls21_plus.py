# !/usr/bin/python
# coding: utf8
# Time: 2019-01-31 16:00
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



