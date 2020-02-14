'''
прочитать строки из файла
сформировать список точек
найти максимально удалённую точку и вывести на экран
'''

import module as m

name_file = input('Введите имя файла: ')

lines = m.get_lines(name_file, 1) # получить линии из файла
points = m.get_points(lines) # получить список точек
print(m.get_max_point(points)) # вывести максимально удалённую
