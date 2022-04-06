import pygame
from factory import Tank
from graph_interface import window

clock = pygame.time.Clock()
FPS = 60

objects = []
tank1 = Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d,
                                   pygame.K_w, pygame.K_s, pygame.K_SPACE), window)
objects.append(tank1)
tank2 = Tank('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT,
                                  pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER), window)
objects.append(tank2)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()

    for obj in objects:
        obj.update(keys)

    window.fill((0, 0, 0))
    for obj in objects:
        obj.create_object()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
