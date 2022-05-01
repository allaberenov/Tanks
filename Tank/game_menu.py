import pygame
import time
import webbrowser

from menu_attributes import Button


def open_menu():
    WIDTH, HEIGHT = 800, 500

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('images/background.jpg')
    window.blit(background, (0, 0))
    pygame.display.update()

    startgame_button = Button(window, 25, 50, "New game", (220, 220, 220))
    feedback_button = Button(window, 25, 120, "Support", (0, 220, 220))
    finishgame_button = Button(window, 25, 190, "Exit", (0, 220, 220))

    buttons = [startgame_button, feedback_button, finishgame_button]

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        for button in buttons:
            button.update()
            if button.pressed() == "New game":
                time.sleep(0.3)
                return True
            elif button.pressed() == "Exit":
                time.sleep(0.3)
                return False
            elif button.pressed() == "Support":
                webbrowser.open('https://vk.com/allaberenov.kerim', new=1)

        pygame.display.update()
