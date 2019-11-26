'''
прочитать строки из файла
сформировать список точек
найти максимально удалённую точку и вывести на экран
'''
# camel-case
# snake-case
name_file = input('Введите имя файла: ')
lines = get_lines(name_file)
points = get_points(lines)
print(get_max_point(points))