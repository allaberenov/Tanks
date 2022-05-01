import time

import pygame

from menu_attributes import Button

imgTanks = [
    pygame.image.load('images/tank1.png'),
    pygame.image.load('images/tank2.png'),
]

WIDTH, HEIGHT = 800, 500


def result_menu(object):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('images/result_background.png')
    window.blit(background, (0, 0))

    myFont = pygame.font.SysFont("Times New Roman", 30, bold=True)
    myText = myFont.render("Player " + str(object.rank+1) + " win!"+"     Last hp: " + str(object.hp), 1, object.color)
    window.blit(myText, (60, 15))
    pygame.display.update()

    window.blit(object.image, (20, 20))

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
            pygame.display.update()
            if button.pressed() == "Main menu":
                return True
            elif button.pressed() == "Exit":
                return False
    time.sleep(0.2)
    pygame.quit()
