'''
    получить имя текущей папки
    распечатать содержимое текущей папки
'''

import os

path = os.curdir  # это ссылка на текущий каталог
print(path)
path = os.getcwd()  # это полный путь к нему
print(path)

list_dir = os.listdir()  # список содержимого текущей папки

print('-'*20)
print('\n'.join(list_dir))  # выводим в столбик

# или циклом
print('-'*20)
for item in list_dir:
    print(item)

print('-' * 20)
for item in list_dir:
    if os.path.isdir(item):
        print('dir - ', item)

print('-' * 20)
for item in list_dir:
    if os.path.isfile(item):
        print('file - ', item)

print('-' * 20)
for item in list_dir:
    if os.path.isfile(item):
        file_name, file_extension = os.path.splitext(item)
        # ext = list(reversed(item.split('.')))[0]
        # print(ext)
        print('name - %s, ext - %s' % (file_name, file_extension))

