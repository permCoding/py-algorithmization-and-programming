import pygame
from init import *
# при падении на ДНО блок получает заливку


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
press_time = 0
int_pressed = 100  # mlsek

while True:
    clock.tick()
    fall_time += clock.get_rawtime()
    press_time += clock.get_rawtime()

    if press_time >= int_pressed:
        press_time = 0
        key = pygame.key.get_pressed()  # checking pressed keys
        if pos_y < cnt_h - 1:  # на дне стакана нельзя двигать блок
            if pos_x > 0 and key[pygame.K_LEFT]:
                pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                pos_x -= 1
            if pos_x < cnt_w - 1 and key[pygame.K_RIGHT]:
                pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
                pos_x += 1

    if fall_time >= interval:
        fall_time = 0
        if pos_y < cnt_h - 1:
            pygame.draw.rect(win, color_bg, (pos_x * r, pos_y * r, r, r), 3)
            pos_y += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    if pos_y < cnt_h - 1: # если ещё не достигли дна
        pygame.draw.rect(win, color_fg, (pos_x * r, pos_y * r, r, r), 3)  # контур квадрата
    else:
        pygame.draw.rect(win, color_fg, (pos_x * r, pos_y * r, r, r))  # заливка квадрата
        pos_y = 1
        pos_x = cnt_w // 2
    
    pygame.display.update()
    
