import pygame
from init import *
# коды клавиш, по одному нажатию клавиши за раз


win = pygame.display.set_mode(sc_size)

while True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
        elif e.type == pygame.KEYDOWN:
            print(e.key)  # код клавиши
        else:
            pass
