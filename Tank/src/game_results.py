import time

import pygame

from menu_attributes import Button

WIDTH, HEIGHT = 800, 500
TEXT_POSITION = (60, 15)

WINNER_IMG_pos = (20, 20)
BUTTON1_pos = (25, 420)
BUTTON2_pos = (200, 420)


def result_menu(object):
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('./../images/result_background.png')
    window.blit(background, (0, 0))
    pygame.display.update()

    pygame.mixer.music.load("./../sounds/result_menu.flac")
    pygame.mixer.music.play(loops=-1)

    myFont = pygame.font.SysFont("Times New Roman", 30, bold=True)

    long_space = '         '
    result_message = "Player " + \
        str(object.rank + 1) + " win!" + \
        long_space + "Last hp: " + str(object.hp)
    myText = myFont.render(result_message, True, object.color)
    window.blit(myText, TEXT_POSITION)

    window.blit(object.image, WINNER_IMG_pos)

    startgame_button = Button(window, BUTTON1_pos, "Main menu", length=155)
    finishgame_button = Button(window, BUTTON2_pos, "Exit", length=155)
    buttons = [startgame_button, finishgame_button]

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

            for button in buttons:
                button.update()
                if button.pressed() == "Main menu" and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop()
                    return True
                if button.pressed() == "Exit" and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop()
                    return False
                pygame.display.update()
    time.sleep(0.2)
    pygame.quit()
