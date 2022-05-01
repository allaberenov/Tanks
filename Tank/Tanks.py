import pygame
import factory

clock = pygame.time.Clock()
FPS = 60

factory.make_player1_tank()
factory.make_player2_tank()

factory.create_blocks(80)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    factory.update_objects(keys)

    factory.create_objects()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
