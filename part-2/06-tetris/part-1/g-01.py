import pygame
from init import *
# пауза для окна + обработка UP DOWN

pygame.init()
pygame.display.set_caption('tetRIS')

win = pygame.display.set_mode(sc_size)

# while True:
#     pass

while True:  # бесконечный цикл с возможностью выхода
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            win.fill(color_fg)
            pygame.display.set_caption('KEYDOWN')
            pygame.display.update()
        elif e.type == pygame.KEYUP:
            win.fill(color_bg)
            pygame.display.set_caption('KEYUP')
            pygame.display.update()
        else:
            pass
