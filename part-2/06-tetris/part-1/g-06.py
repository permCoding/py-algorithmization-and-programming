import pygame
from init import *
# смещение фигуры, отслеживание интервала


pygame.init()
pygame.display.set_caption('tetRIS')
win = pygame.display.set_mode(sc_size)
win.fill(color_bg)

pos_x = cnt_w // 2
pos_y = 1
pygame.draw.rect(win, color_fg, (pos_x*r, pos_y*r, r, r), 3)
pygame.display.update()

clock = pygame.time.Clock()
fall_time = 0
interval = 300  # mlsek

while True:
    clock.tick()
    fall_time += clock.get_rawtime()
    print(fall_time)

    if fall_time >= interval:
        fall_time = 0
        pos_y += 1
        pygame.draw.rect(win, color_fg, (pos_x * r, pos_y * r, r, r), 3)
        pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
