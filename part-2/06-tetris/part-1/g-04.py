import pygame
from init import *
# обработка удержания клавиши


win = pygame.display.set_mode(sc_size)

while True:
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_SPACE]:
        print('space')
    if keys[pygame.K_RETURN]:
        print('return')
    if keys[pygame.K_UP]:
        print('up')
    if keys[pygame.K_DOWN]:
        print('down')
    if keys[pygame.K_LEFT]:
        print('left')
    if keys[pygame.K_RIGHT]:
        print('right')
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    pygame.time.delay(100)  # mlsek

