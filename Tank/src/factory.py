import pygame

from graph_interface import window, TILE, TANK_SIZE, UI
from random import randint

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]
ui = UI()

PLAYER_NUMBER = [0, 1]


class Storage:
    objects = []
    bullets = []


class Singleton(Storage):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls


storage = Singleton()

'''Тектуры для объектов'''
imgBrick = pygame.image.load('./../images/block_brick.png')
imgLiana = pygame.image.load('./../images/block_liana.png')
imgIron = pygame.image.load('./../images/block_iron.png')
BLOCK_TYPES = ['block_brick', 'block_liana', 'block_iron']
imgTanks = [
    pygame.image.load('./../images/tank1.png'),
    pygame.image.load('./../images/tank2.png'),
]
imgBangs = [
    pygame.image.load('./../images/bang1.png'),
    pygame.image.load('./../images/bang2.png'),
    pygame.image.load('./../images/bang3.png'),
]

'''Звуки для объектов'''
Tanksounds = [
    pygame.mixer.Sound("./../sounds/tank_shot.wav"),
    pygame.mixer.Sound("./../sounds/explosion.wav"),
    # pygame.mixer.Sound("./../sounds/driving.wav")
]


class Factory:
    def create_objects(self):
        raise NotImplementedError("Функция не переопределена")

    def update(self, *args):
        raise NotImplementedError("Функция не переопределена")


class Tank(Factory):
    def __init__(self, color, px, py, direct, keylist, player_number):
        self.type = 'tank'
        storage.objects.append(self)
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

        self.rank = player_number
        self.image = pygame.transform.rotate(
            imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, keys, *args):
        self.image = pygame.transform.rotate(
            imgTanks[self.rank], -self.direct * 90)
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center=self.rect.center)

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
            if obj != self and (obj.type == BLOCK_TYPES[0] or obj.type == BLOCK_TYPES[2] or obj.type == 'tank') and obj.rect.colliderect(self.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery,
                   dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0:
            self.shotTimer -= 1

    def create_objects(self):
        window.blit(self.image, self.rect)

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
        Tanksounds[0].play()

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > window.get_width() or self.py < 0 or self.py > window.get_height():
            storage.bullets.remove(self)
        else:
            for obj in storage.objects:
                if obj != self.parent and obj.type != 'bang' and obj.type != 'block_liana' and obj.rect.collidepoint(
                        self.px, self.py):
                    obj.damage(self.damage)
                    storage.bullets.remove(self)
                    Bang(self.px, self.py)
                    break

    def create_objects(self):
        pygame.draw.circle(window, 635610, (self.px, self.py), 2)


class Bang(Factory):
    def __init__(self, px, py):
        storage.objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0
        Tanksounds[1].play()

    def update(self, *args):
        self.frame += 0.2
        if self.frame >= 3:
            storage.objects.remove(self)

    def create_objects(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center=(self.px, self.py))
        window.blit(image, rect)


class Block(Factory):
    def __init__(self, px, py, size, type):
        storage.objects.append(self)
        self.type = type

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self, *args):
        pass

    def create_objects(self):
        if self.type == 'block_liana':
            window.blit(imgLiana, self.rect)

        if self.type == 'block_brick':
            window.blit(imgBrick, self.rect)

        if self.type == 'block_iron':
            window.blit(imgIron, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.type == BLOCK_TYPES[2]:
            return
        if self.hp <= 0:
            storage.objects.remove(self)


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
    Tank((0, 250, 0), 100, 275, 0, (pygame.K_a, pygame.K_d,
                                    pygame.K_w, pygame.K_s, pygame.K_SPACE), PLAYER_NUMBER[0])


def make_player2_tank():
    Tank((0, 0, 255), 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_RCTRL),
         PLAYER_NUMBER[1])


def create_blocks(N):
    for _ in range(N):
        while True:
            x = randint(0, window.get_width() // TILE - 1) * TILE - 1
            y = randint(1, window.get_height() // TILE - 1) * TILE - 1
            rect = pygame.Rect(x, y, TILE, TILE)
            fined = False
            for obj in storage.objects:
                if rect.colliderect(obj.rect):
                    fined = True

            if not fined:
                break

        Block(x, y, TILE, BLOCK_TYPES[randint(0, 2)])


def get_winnter():
    number_of_tanks = 0
    for winner in storage.objects:
        if winner.type == 'tank':
            number_of_tanks += 1
    if number_of_tanks == 1:
        for winner in storage.objects:
            if winner.type == 'tank':
                return winner
    else:
        return False


def free_cache():
    storage.objects = []
    storage.bullets = []
