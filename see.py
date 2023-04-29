import pygame, sys
import random
from classBu import *

pygame.init()
w, h = 1000, 1000
wind = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()

n = 80

up = Bulls(w//2, h//3 - n, wind)
down_left = Bulls(w//3 - n, h//3 + h//3, wind)
down_right = Bulls(w//3 + w//3 - n, h//3 + h//3, wind)

point = [up, down_left, down_right]

le = []

x, y = down_right.x, down_right.y

spe = 3

ze = CC(down_left.x, down_left.y, down_right.x, down_right.y)

while True:
    clock.tick(60)
    wind.fill('white')

    for draw in point:
        draw.draw()

    pygame.draw.rect(wind, (170, 30, 30), (x, y - 2.5, 5, 5))
    pygame.draw.line(wind, (0, 0, 0), (up.x, up.y), (x + 2.5, y), 1)


    if x == down_right.x:
        moveTL = True
    elif x == down_left.x:
        moveTL = False
    
    if x > down_left.x and moveTL == True:
        x -= spe
    else:
        x += spe

    middepoint = CC(x, y, up.x, up.y)
    mas = [abs(middepoint[0]), abs(middepoint[1] - up.y)]
    print(f"mas: {mas}")
    print(f'x, y: {[x, y]}')
    z = mas[0]/2
    r = mas[1]/2

    pygame.draw.line(wind, (0, 0, 0), (down_left.x + ze[0] / 2, down_left.y), (x + 2.5, y), 1)
    pygame.draw.line(wind, (0, 0, 0), (down_left.x + ze[0] / 2, down_left.y), (x + 2.5, y), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
