import pygame
import time
import webbrowser

from menu_attributes import Button

BUTTON1_pos = (25, 50)
BUTTON2_pos = (25, 120)
BUTTON3_pos = (25, 190)
BUTTON4_pos = (25, 250)
pygame.mixer.music.load("./sounds/World of Tanks .mp3")


def open_menu():
    WIDTH, HEIGHT = 800, 500
    clock = pygame.time.Clock()
    FPS = 60

    window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.init()
    pygame.display.set_caption("*****Tanks*****")
    background = pygame.image.load('./images/background.jpg')
    window.blit(background, (0, 0))
    pygame.display.update()
    pygame.mixer.music.play(loops=-1, fade_ms=1)

    startgame_button = Button(window, BUTTON1_pos, "New game")
    sound_button = Button(window, BUTTON2_pos, "Voiced")
    feedback_button = Button(window, BUTTON3_pos, "Support")
    finishgame_button = Button(window, BUTTON4_pos, "Exit")

    buttons = [startgame_button, feedback_button, sound_button, finishgame_button]

    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            for button in buttons:
                button.update()
                if button.pressed() == "New game" and event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.music.stop()
                    return True
                if event.type == pygame.MOUSEBUTTONDOWN and button.pressed() == "Voiced":
                    pygame.mixer.music.pause()
                    button.text = "Mute"
                    pygame.display.update()
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and button.pressed() == "Mute":
                    pygame.mixer.music.unpause()
                    button.text = "Voiced"
                    pygame.display.update()
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN and button.pressed() == "Exit":
                    time.sleep(0.1)
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN and button.pressed() == "Support":
                    webbrowser.open('https://vk.com/allaberenov.kerim', new=1)
                    continue

        pygame.display.update()
        clock.tick(FPS)
