import pygame
from graph_interface import WIDTH, HEIGHT
DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
TILE = 32


class Factory:
    def create_object(self):
        raise NotImplementedError("Функция не переопределена")


class Tank(Factory):
    def __init__(self, color, px, py, direct, keyList, window):
        self.type = 'tank'
        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 6
        self.window = window

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

    def update(self, keys):
        if keys[self.keyLEFT] and self.rect.x > 0:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT] and self.rect.x < WIDTH - TILE:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP] and self.rect.y > 0:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN] and self.rect.y < HEIGHT - TILE:
            self.rect.y += self.moveSpeed
            self.direct = 2

    def create_object(self):
        pygame.draw.rect(self.window, self.color, self.rect)

        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(self.window, 'white', self.rect.center, (x, y), 4)
