from random import randint

import pygame

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
TILE = 32

pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))


class Factory:
    objects = []
    bullets = []


factory = Factory()


class Creator(Factory):
    def create_objects(self):
        raise NotImplementedError("Функция не переопределена")


class Tank(Creator):
    def __init__(self, color, px, py, direct, keylist):
        Factory.objects.append(self)
        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2
        self.hp = 1

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

        for obj in Factory.objects:
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
            Factory.objects.remove(self)
            print(self.color, 'dead')


class Bullet(Creator):
    def __init__(self, parent, px, py, dx, dy, damage):
        Factory.bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > WIDTH - TILE or self.py < 0 or self.py > HEIGHT:
            Factory.bullets.remove(self)
        else:
            for obj in Factory.objects:
                if obj != self.parent and obj.rect.collidepoint(self.px, self.py):
                    # obj.damage(self.damage)
                    Factory.bullets.remove(self)
                    Factory.objects.remove(obj)
                    break

    def create_objects(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)

class Block:
    def __init__(self, px, py, size):
        Factory.objects.append(self)
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
        if self.hp <= 0: Factory.objects.remove(self)


# class B

def create_objects():
    window.fill((0, 0, 0))
    for bullet in factory.bullets:
        bullet.create_objects()
    # if len(bullets) == 0:
    #        print('Массив пуль пуст')
    for obj in factory.objects:
        obj.create_objects()


def update_objects(keys):
    for bullet in factory.bullets:
        bullet.update()
        # print(bullet)
    for obj in factory.objects:
        obj.update(keys)


def make_player1_tank():
    Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))


def make_player2_tank():
    Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER))

def create_blocks(N):
    for _ in range(N):
        while True:
            x = randint(0, WIDTH // TILE - 1) * TILE
            y = randint(0, HEIGHT // TILE - 1) * TILE
            rect = pygame.Rect(x, y, TILE, TILE)
            fined = False
            for obj in Factory.objects:
                if rect.colliderect(obj.rect): fined = True

            if not fined: break

        Block(x, y, TILE)
