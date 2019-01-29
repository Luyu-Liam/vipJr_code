import random

# result = 0 # 0表示没猜中，1表示猜中了。初始的时候为0

# while result == 0:
#     target = random.randint(1, 6)
#     guess = int(input('你猜猜看是多少？\n'))
#     if target == guess:   # 猜中了
#         result = 1
#         print('你怎么这么牛逼，恭喜你猜对了')
#     else: # 没猜中
#         result = 0
#         print('你这个菜鸡，猜错了，重来！！！')
#     print('骰子的点数为：%d' % target)
#     print('*'*50)


# 下面的代码为三个骰子的情况，如果需要运行，请先将上面的代码注释掉，然后取消下面的代码的注释。
# import random
# result = 0
# while result == 0:
#     target1 = random.randint(1, 6)
#     target2 = random.randint(1, 6)
#     target3 = random.randint(1, 6)
#     target = target1 + target2 + target3
#     guess = int(input('你猜是多少？\n'))
#     if guess == target:
#         print('猜对了')
#         result = 1
#     else:
#         print('猜错了，重来一次')
#         result = 0
#     print('三个骰子的点数分别为：%d %d %d' %(target1, target2, target3))
#     print('*'*50)
# print('恭喜你，猜对了')
# print('*'*50)


# 剪刀石头布
import random
flag = 1

while flag == 1:
    player = int(input("请输入剪刀石头布（0剪刀-1石头-2布）："))
    computer = random.randint(0, 2)
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        flag = 2
        print("赢了，可以去买奶粉了...")
    elif player == computer:
        flag = 1
        print('平局，，，洗洗手决战到天亮。。')
    else:
        flag = 1
        print('输了，回家拿钱，再来。。')

























