import pygame
from factory import Tank, Bullet, Factory, update_objects, create_objects, make_player1_tank, make_player2_tank, create_blocks

clock = pygame.time.Clock()
FPS = 60

make_player1_tank()
make_player2_tank()

create_blocks(20)
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    update_objects(keys)
    create_objects()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
