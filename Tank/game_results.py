import pygame
import time
import menu_attributes
import factory

from menu_attributes import Button


imgTanks = [
    pygame.image.load('images/tank1.png'),
    pygame.image.load('images/tank2.png'),
]

WIDTH, HEIGHT = 800, 500


def result_menu(objects):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('images/result_background.png')
    window.blit(background, (0, 0))
    pygame.display.update()

    startgame_button = Button(window, 25, 420, "Main menu", (0, 220, 220), length=155)
    finishgame_button = Button(window, 200, 420, "Exit", (0, 220, 220), length=155)
    buttons = [startgame_button, finishgame_button]




    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        for button in buttons:
            button.update()
            if button.pressed() == "Main menu":
                return True
            elif button.pressed() == "Exit":
                return False

        pygame.display.update()
    pygame.quit()

