import pygame

pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
TILE = 32
TANK_SIZE = 31

fontUI = pygame.font.Font(None, 30)

class UI:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self, objects):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.hp), True, obj.color)
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1
