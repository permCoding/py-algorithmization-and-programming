import pygame


def printing():
    win.blit(image_bg, (0, 0))  # рисуем фон на окне
    win.blit(images[img_index], (pos_x, pos_y))  # рисуем человека поверх фона
    pygame.display.update()  # обновляем окно

pygame.init()

image_bg = pygame.image.load('bg1200.jpg')  # загружаем фон игры
win_width, win_height = image_bg.get_rect().size  # узнаём размеры фона
win_size = (win_width, win_height)  # запоминаем размеры
win = pygame.display.set_mode(win_size)  # делаем окно по размерам фона
win.blit(image_bg, (0, 0))  # рисуем фон на окне

img_names = [
    'orange/0.png','orange/1.png','orange/2.png','orange/3.png','orange/4.png'
]  # имена рисунков шагов человека
images = []  # список для хранения самих рисунков
for name in img_names:
    images.append(pygame.image.load(name).convert_alpha())

img_index = 0  # индекс текущего образа человека
h_w, h_h = images[img_index].get_rect().size  # размеры рисунка человека
step = h_w // 3  # размер шага человека
pos_x = 150  # начальная позиция X человека
pos_y = win_height - h_h - 135  # начальная позиция Y человека
win.blit(images[img_index], (pos_x, pos_y))  # рисуем текущий образ человека

pygame.display.update()  # обновляем окно

clock = pygame.time.Clock()  # объект для фиксации промежутков времени
press_time = 0  # время удержания клавиши нажатой
int_pressed = 100  # интервал паузы, потом смещение человека в mlsek

while True:  # бесконечный цикл приложения, для обработки событий
    clock.tick()  # в каждой итерации фиксируем время
    press_time += clock.get_rawtime()  # накапливаем время удержания

    if press_time > int_pressed:  # если превысили интервал паузы
        press_time = 0  # сбрасываем для следующего цикла удержания
        key = pygame.key.get_pressed()  # узнаём какая клавиша нажата
        if pos_x > h_w and key[pygame.K_LEFT]:
            pos_x -= step  # движение влево
            img_index = (img_index - 1) % len(images)
            printing()
        if pos_x + step < win_width - h_w and key[pygame.K_RIGHT]:
            pos_x += step  # движение вправо
            img_index = (img_index + 1) % len(images)  # 0 1 2 3 4 -> 5 => 0 1 2 3 4
            printing()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:  # если нажали ВЫХОД
            pygame.quit()


