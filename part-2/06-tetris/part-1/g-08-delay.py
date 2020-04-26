import pygame
from init import *
# подение фигуры, затирание старой фигуры - стирается весь фон, delay


pygame.init()
pygame.display.set_caption('tetRIS')
win = pygame.display.set_mode(sc_size)
win.fill(color_bg)

pos_x = cnt_w // 2
pos_y = 1
pygame.draw.rect(win, color_fg, (pos_x*r, pos_y*r, r, r), 3)
pygame.display.update()

interval = 300  # mlsek

while True:
    pygame.time.delay(interval)  # просто задержка в игре

    if pos_y < cnt_h - 1:
        win.fill(color_bg)
        pos_y += 1
        pygame.draw.rect(win, color_fg, (pos_x * r, pos_y * r, r, r), 3)
        pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
