'''
    рекурсивный перебор файлов в подкаталогах
    и вывод их имён на экран
'''

import os

def print_list(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            print_list(path)


path = os.curdir  # это ссылка на текущий каталог
# path = os.getcwd()  # это полный путь к нему
print(path)
print_list(path)
