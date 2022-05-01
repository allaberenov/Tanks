import pygame
import time
import webbrowser

from menu_attributes import Button

BUTTON1_pos = (25, 50)
BUTTON2_pos = (25, 120)
BUTTON3_pos = (25, 190)


def open_menu():
    WIDTH, HEIGHT = 800, 500

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('../images/background.jpg')
    window.blit(background, (0, 0))
    pygame.display.update()

    startgame_button = Button(window, BUTTON1_pos, "New game")
    feedback_button = Button(window, BUTTON2_pos, "Support")
    finishgame_button = Button(window, BUTTON3_pos, "Exit")

    buttons = [startgame_button, feedback_button, finishgame_button]

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        for button in buttons:
            button.update()
            if button.pressed() == "New game":
                time.sleep(0.1)
                return True
            elif button.pressed() == "Exit":
                time.sleep(0.1)
                return False
            elif button.pressed() == "Support":
                webbrowser.open('https://vk.com/allaberenov.kerim', new=1)

        pygame.display.update()
