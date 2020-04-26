import pygame


pygame.init()

screen = pygame.display.set_mode((400, 200))
font = pygame.font.SysFont('Consolas', 36)
color_bg = (255, 255, 255)
color_fg = (0, 0, 55)

seconds = 0
text = str(seconds)
start_ticks = pygame.time.get_ticks()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            run = False

    temp_ticks = pygame.time.get_ticks()
    if seconds != (temp_ticks - start_ticks) // 1000:
        seconds = (temp_ticks - start_ticks) // 1000
        text = str(seconds)

    screen.fill(color_bg)
    screen.blit(font.render(text, True, color_fg), (100, 50))
    pygame.display.update()

pygame.quit()
