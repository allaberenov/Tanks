import pygame

import factory
import game_menu

clock = pygame.time.Clock()
FPS = 60


def play_game():
    play = True

    if not game_menu.open_menu():
        play = False

    factory.make_player1_tank()
    factory.make_player2_tank()
    factory.create_blocks(80)

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        keys = pygame.key.get_pressed()

        factory.update_objects(keys)

        factory.create_objects()

        pygame.display.update()
        clock.tick(FPS)
        winner = factory.get_winnter()

        if winner:
            return True