import pygame, sys
import random
from classBu import *

pygame.init()
w, h = 1000, 1000
wind = pygame.display.set_mode((w, h))

clock = pygame.time.Clock()


Po1 = Bulls(random.randint(20, w - 20), random.randint(20, h - 20), wind)
Po2 = Bulls(random.randint(20, w - 20), random.randint(20, h - 20), wind)
Po3 = Bulls(random.randint(20, w - 20), random.randint(20, h - 20), wind)



point = [Po1, Po2, Po3]

le = []

maxing = 1000000

#move point
x, y = random.randint(20, w - 20), random.randint(20, h - 20)

while True:
    clock.tick(60)
    wind.fill('white')
    pygame.draw.circle(wind, (170, 0, 0), [x, y], 4)
    
    for draw in point:
        draw.draw()

    
    ranPoint = point[random.randint(0, len(point)-1)]
    move = CC(x, y, ranPoint.x, ranPoint.y)
    print(move)
    x += move[0]/2
    y += move[1]/2
    le.append(pygame.Rect(x, y, 4, 4))

    for rect in le:
        pygame.draw.rect(wind, (170, 0, 0), rect)

    if len(le) >= maxing:
        break
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
