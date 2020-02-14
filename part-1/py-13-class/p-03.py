'''
прочитать строки из файла
сформировать список точек
найти максимально удалённую точку и вывести на экран
'''
# camel-case
# snake-case

import module as m

name_file = input('Введите имя файла: ')
lines = m.get_lines(name_file, 1)
print('\n'.join(lines))

# points = m.get_points(lines)
# print(m.get_max_point(points))
