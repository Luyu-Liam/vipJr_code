# !/usr/bin/python
# coding: utf8
# @Time    : 2018-11-07 14:57
# @Author  : Liam
# @Email   : luyu.real@qq.com
# @Software: PyCharm
#                        .::::.
#                      .::::::::.
#                     :::::::::::
#                  ..:::::::::::'
#               '::::::::::::'
#                 .::::::::::
#            '::::::::::::::..
#                 ..::::::::::::.
#               ``::::::::::::::::
#                ::::``:::::::::'        .:::.
#               ::::'   ':::::'       .::::::::.
#             .::::'      ::::     .:::::::'::::.
#            .:::'       :::::  .:::::::::' ':::::.
#           .::'        :::::.:::::::::'      ':::::.
#          .::'         ::::::::::::::'         ``::::.
#      ...:::           ::::::::::::'              ``::.
#     ```` ':.          ':::::::::'                  ::::..
#                        '.:::::'                    ':'````..
#                     美女保佑 永无BUG
import random
import sys
import pygame

def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    """
    屏幕上显示一些内容
    :param scr: 显示的地方
    :param font: 字体
    :param x: 位置坐标x
    :param y: 位置坐标y
    :param text: 文本内容
    :param color: 颜色
    """
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))

def playGame(scr, lives, score):
    """
    游戏函数
    :param scr: 载体
    :param lives: 生命数
    :param score: 分数
    :return: 返回当前生命值和分数
    """
    font1 = pygame.font.Font(None, 24)  # 显示的字体
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40  # 接球板的大小和位置
    ball_x, ball_y = random.randint(0, 500), 0  # 球的初始位置
    vel_y = 0.1  # 球下落的速度
    white = 255, 255, 255
    # 给球设定随机的颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                rect_x, _ = event.pos
                if rect_x < 0:
                    rect_x = 0
                elif rect_x > 600 - rect_w:
                    rect_x = 600 - rect_w

        # 加上键盘的控制
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_RIGHT]:
            rect_x += 0.5
        elif keys[pygame.K_LEFT]:
            rect_x -= 0.5

        scr.fill(white)
        pygame.draw.rect(scr, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)
        ball_y += vel_y
        if ball_y > 500:
            # 没接住
            lives -= 1
            ball_x = random.randint(0, 500)
            ball_y = 0
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            # vel_y = vel_y - score/50  # 没接住时速度缓冲一下
        elif (rect_y - ball_y) < 30 and rect_x < ball_x < (rect_x + rect_w):
            # 接住了
            score += 1
            vel_y = 0.1 + score/50
            ball_x = random.randint(0, 500)
            ball_y = 0
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
        else:
            ball_y += vel_y
        pygame.draw.circle(scr, [r, g, b], (int(ball_x), int(ball_y)), 30, 0)
        print_text(scr, font1, 0, 0, "Lives: "+str(lives))
        print_text(scr, font1, 500, 0, "Score: "+str(score))
        pygame.display.update()
    return lives, score


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drop Ball")
font1 = pygame.font.Font(None, 24)
lives, score = 3, 0
while True:
    lives, score = playGame(screen, lives, score)
    print(lives, score)
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONUP:
            lives = 3
            score = 0
        elif e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill([255, 255, 0])
    print_text(screen, font1, 250, 250, 'GAME OVER!')
    print_text(screen, font1, 240, 270, 'Score:{} <Replay>'.format(str(score)))
    pygame.display.update()
    
