import pygame
import random
def main():
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('BALL')
    ball_x = 0
    ball_y = 0
    color = [255, 10, 20]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, color, (ball_x, ball_y), 30, 0)
        ball_x += 1
        ball_y += 1
        if ball_x == 800:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color[0] = r
            color[1] = g
            color[2] = b
            ball_x = 0
            ball_y = 0
        pygame.display.update()

main()





