'''
прочитать строки из файла
сформировать список точек
найти максимально удалённую точку и вывести на экран

сигнатура метода - кол-во и типы аргументов фу

проектирование сверху-вниз - водопадное
'''

import module as m

name_file = input('Введите имя файла: ')

lines = m.get_lines(name_file, 1) # получить линии из файла

points = m.get_points(lines) # получить список точек

# print(points)
for point in points:
	print(point)

max_point = m.get_max_point(points) # получить максимально удалённую
print(max_point)