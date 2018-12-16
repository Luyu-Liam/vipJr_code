# !/usr/bin/python
# coding: utf8
# @Time    : 2018-12-15 20:09
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm
"""
这节课是关于if分支结构、for循环结构、while循环结构的复习课。
"""


"""
1.  输入一个分数（0~100），通过python编程对其进行等级划分，规则如下：
    90以上（包含90）： -------------------A
    80~90（包含80）：--------------------B
    70~80（包含70）：--------------------C
    60~70（包含60）：--------------------D
    60以下（不包含60）：------------------E
    如果输入的分数不合法（超过100或者低于0），则输出“Error”
"""
score = int(input("请输入一个分数："))
if score > 100 or score < 0:
    print('Error')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')


"""
2. 输入三个整数a, b, c，请把这三个数由小到大输出。
"""
a, b, c = int(input()), int(input()), int(input())
if a > b:
    a, b = b, a   # 交换a, b两个数
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a, b, c)

"""
3. 输出九九乘法表
"""
for i in range(1, 10):
    result = ""
    for j in range(1, i+1):
        result += "%d x %d = %d\t" % (j, i, i*j)
    print(result)

"""
4. 还记得课堂上的“猜大小”游戏吗？让计算机产生一个1~6的随机数，用户进行猜测，如果猜不中则继续猜，直到猜中为止。
现在请你编程实现它，想想该用哪种 循环结构？
"""
import random
flag = False   # 状态标识量，False表示没猜对，True表示猜中了
while not flag:
    number = random.randint(1, 6)
    your_answer = int(input("猜猜看"))
    if your_answer == number:
        flag = True
        print('恭喜你，猜对了')
    else:
        flag = False
    print('the real number is %d' %number)
    print("*"*55)

"""
5. 判断101~200之间有多少个素数，并输出所有素数。
"""
# for循环来做
for number in range(101, 201):
    for i in range(2, number):
        if number % i == 0:   # 一旦发现2~number-1的范围有数字可以被number除尽，则说明不是质数，循环停止
            break
    else:
        print(number)

# while循环来做
number = 101
flag = True
while number < 201:
    i = 2
    while i < number:
        if number % i == 0:
            break
        i += 1
    else:
        print(number)
    number += 1

