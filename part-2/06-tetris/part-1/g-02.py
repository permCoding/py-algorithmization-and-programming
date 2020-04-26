import pygame
from init import *
# пауза для окна + выход по KEYUP ESC


win = pygame.display.set_mode(sc_size)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or \
                e.type == pygame.KEYUP and \
                e.key == pygame.K_ESCAPE:
            print('key_esc')
            run = False
        else:
            print('key_down')

pygame.quit()
