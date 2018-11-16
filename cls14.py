import random
import sys
import pygame

def print_text(scr, font, x, y, text, color=(250, 25, 255)):
    imgText = font.render(text, True, color)
    scr.blit(imgText, (x, y))

def playGame(scr, lives, score):
    font1 = pygame.font.Font(None, 24)
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40
    ball_x, ball_y = random.randint(0, 500), -50
    vel_y = 4
    white = 255, 255, 255
    while lives > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                rect_x, _ = event.pos
                if rect_x < 0:
                    rect_x = 0
                elif rect_x > 600 - rect_w:
                    rect_x = 600 - rect_w
        scr.fill(white)
        pygame.draw.rect(scr, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)

        print_text(scr, font1, 0, 0, "Lives: "+str(lives))
        print_text(scr, font1, 500, 0, "Score: "+str(score))
        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drop Ball")
font1 = pygame.font.Font(None, 24)
playGame(screen, 3, 0)



