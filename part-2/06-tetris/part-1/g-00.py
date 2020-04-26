'''
заготовка под тетрис
вертикальный стакан + внутри блоки падают сверху-вниз
блок - пока просто квадрат
'''

import pygame
# просто окно приложения - закрывается


r = 50  # сторона блока в пискелях
cnt_w = 9  # ширина стакана в блоках
cnt_h = 16  # высота стакана
sc_width = r * cnt_w  # ширина экрана в пикселях
sc_height = r * cnt_h  # высота экрана
sc_size = (sc_width, sc_height)  #
color_bg = (0, 55, 99)  # цвет фона
color_fg = (225, 125, 0)  # цвет контура


pygame.display.set_caption('tetRIS')

win = pygame.display.set_mode(sc_size)
win.fill(color_bg)

pygame.display.update()

