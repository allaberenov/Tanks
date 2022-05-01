import pygame

import factory
import game_results
import play

while True:
    if not play.play_game():
        pygame.quit()
        break
    if not game_results.result_menu(factory.get_winnter()):
        pygame.quit()
        break
    factory.free_cache()
