import pygame

class Bulls:

    def __init__(self, x, y, wind):
        self.x = x
        self.y = y
        self.wind = wind

    def draw(self):
        pygame.draw.circle(self.wind, (255, 90, 90), (self.x, self.y), 6)



def CC(X1, Y1, X2, Y2):
    return [(X2 - X1), (Y2 - Y1)]

