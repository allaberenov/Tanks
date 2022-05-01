import pygame

import factory
import game_menu


def play_game():
    clock = pygame.time.Clock()
    FPS = 60

    play = True

    BLOCKS_NUMBER = 160

    if not game_menu.open_menu():
        play = False

    factory.make_player1_tank()
    factory.make_player2_tank()
    factory.create_blocks(BLOCKS_NUMBER)

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
