import pygame
from init import *
# обработка нажатий ВЛЕВО-ВПРАВО, по одной клавише, на дне стакана НЕЛЬЗЯ двигать 


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

    if fall_time >= interval:
        fall_time = 0
        if pos_y < cnt_h - 1:
            pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
            pos_y += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            if pos_y < cnt_h - 1:  # на дне стакана нельзя двигать блок
                pygame.draw.rect(win, color_bg, (pos_x*r, pos_y*r, r, r), 3)
                if pos_x > 0 and e.key == pygame.K_LEFT:
                    pos_x -= 1
                elif pos_x < cnt_w - 1 and e.key == pygame.K_RIGHT:
                    pos_x += 1

    pygame.draw.rect(win, color_fg, (pos_x * r, pos_y * r, r, r), 3)
    pygame.display.update()
