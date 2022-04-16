from random import randint
from graph_elements import window, TILE, TANK_SIZE, UI
import pygame

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ui = UI()

class Storage:
    objects = []
    bullets = []


storage = Storage()


class Factory:
    def create_objects(self):
        raise NotImplementedError("Функция не переопределена")

    def update(self, *args):
        raise NotImplementedError("Функция не переопределена")


class Tank(Factory):
    def __init__(self, color, px, py, direct, keylist):
        Storage.objects.append(self)
        self.type = 'tank'
        self.color = color
        self.rect = pygame.Rect(px, py, TANK_SIZE, TANK_SIZE)
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 5

        self.shotTimer = 0
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = keylist[0]
        self.keyRIGHT = keylist[1]
        self.keyUP = keylist[2]
        self.keyDOWN = keylist[3]
        self.keySHOT = keylist[4]

    def update(self, keys):
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT] and self.rect.x >= 0:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT] and self.rect.x <= window.get_width() - TILE:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP] and self.rect.y >= 0:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN] and self.rect.y <= window.get_height() - TILE:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in storage.objects:
            if obj != self and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1

    def create_objects(self):
        pygame.draw.rect(window, self.color, self.rect)

        x = self.rect.centerx + DIRECTS[self.direct][0] * 30
        y = self.rect.centery + DIRECTS[self.direct][1] * 30
        pygame.draw.line(window, 'white', self.rect.center, (x, y), 4)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            storage.objects.remove(self)
            print(self.color, 'dead')


class Bullet(Factory):
    def __init__(self, parent, px, py, dx, dy, damage):
        storage.bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > window.get_width() or self.py < 0 or self.py > window.get_height():
            storage.bullets.remove(self)
        else:
            for obj in Storage.objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    obj.damage(self.damage)
                    Storage.bullets.remove(self)
                    #Storage.objects.remove(obj)
                    break

    def create_objects(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)


class Block(Factory):
    def __init__(self, px, py, size):
        storage.objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self, *args):
        pass

    def create_objects(self):
        pygame.draw.rect(window, 'green', self.rect)
        pygame.draw.rect(window, 'gray20', self.rect, 2)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: storage.objects.remove(self)


# class B

def create_objects():
    window.fill((0, 0, 0))
    for bullet in storage.bullets:
        bullet.create_objects()
    for obj in storage.objects:
        obj.create_objects()
    ui.draw(storage.objects)


def update_objects(keys):
    for bullet in storage.bullets:
        bullet.update()
        # print(bullet)
    for obj in storage.objects:
        obj.update(keys)
    ui.update()

def make_player1_tank():
    Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))


def make_player2_tank():
    Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL))


def create_blocks(N):
    for _ in range(N):
        while True:
            x = randint(0, window.get_width() // TILE - 1) * TILE - 1
            y = randint(1, window.get_height() // TILE - 1) * TILE - 1
            rect = pygame.Rect(x, y, TILE, TILE)
            fined = False
            for obj in storage.objects:
                if rect.colliderect(obj.rect): fined = True

            if not fined: break

        Block(x, y, TILE)