import pygame
from init import *
# рисуем на форме примитивы


pygame.init()
pygame.display.set_caption('tetRIS')
win = pygame.display.set_mode(sc_size)
win.fill(color_bg)

pos_x = cnt_w // 2
pos_y = 1
pygame.draw.rect(win, color_fg, (pos_x*r, pos_y*r, r, r), 3)

pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
