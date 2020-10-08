import pygame
import random


pygame.init()

image_bg = pygame.image.load('bg_nebo.jpg')  # фон
win_width, win_height = image_bg.get_rect().size  # размеры
win_size = (win_width, win_height)  # запоминаем размеры
win = pygame.display.set_mode(win_size)  # устанавливаем размеры окна
win.blit(image_bg, (0, 0))  # заливаем фон

bomb_names = ['bombs/red.png','bombs/green.png']  # имена рисунков бобмочек
bomb_images = []
for item in bomb_names:  # добавляем сами рисункци в список
    bomb_images.append(
        pygame.image.load(item).convert_alpha()
    )
    # bomb_images.append(
    #     pygame.transform.scale(
    #         pygame.image.load(item).convert_alpha(),
    #         (40,40)  # можно изменить размеры
    #     )
    # )

bomb_count = 50  # количество бомбочек
bomb_list = []  # список бобмочек - как спавн препятствий
spavn_y = 0  # начальный отступ между бомбочками
for _ in range(bomb_count):
    img = random.choice(bomb_images)  # случайный рисунок бомбочки
    x = random.randint(40, win_width-40)  # случайный отступ по X
    spavn_y += int(1.0 * random.randint(0, win_height))
    y = 25 - spavn_y  # отступ по Y с накоплением от предыдущей бомбочки
    v = random.randint(1, 10)  # случайная скорость падения
    bomb = [img, x, y, v, True]  # для каждой бомбочки свои параметры
    bomb_list.append(bomb)  # добавляем бомбу в список

clock = pygame.time.Clock()  # объект для отсчёта времени
time_fall = 0  # текущее время задержки падения всех бомбочек
int_fall = 20  # интервал до следующего сдвига mlsek

pygame.display.update()  # отрисовываем фон

run = True
while run:  # бесконечный цикл приложения, для обработки событий

    clock.tick()  # в каждой итерации фиксируем время
    time_fall += clock.get_rawtime()  # накапливаем время паузы
    if time_fall >= int_fall:  # если превысили интервал паузы
        time_fall = 0  # сбрасываем для следующего цикла паузы
        for i in range(bomb_count):  # для всех бомб из списка
            if bomb_list[i][4]:  # если бомба ещё не достигла дна
                bomb_list[i][2] += bomb_list[i][3]  # смещаем её на шаг

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если нажали ВЫХОД
            run = False

    win.blit(image_bg, (0, 0))  # рисуем фон на окне
    for i in range(bomb_count):  # для всех бомб из списка
        if bomb_list[i][4]:  # если бомба ещё не достигла дна
            win.blit(bomb_list[i][0], (bomb_list[i][1], bomb_list[i][2]))  # рисуем бомбу
            if bomb_list[i][2] > win_height - 216:  # если бомба достигла дна
                bomb_list[i][4] = False  # отключаем бомбу

    pygame.display.update()  # отрисовываем всё

pygame.quit()
