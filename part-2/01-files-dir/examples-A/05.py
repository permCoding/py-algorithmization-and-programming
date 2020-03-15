'''
    перебор файлов в подкаталогах
    формирование списка файлов по фильтру csv и печать их содержимого
'''

import os

def get_list_ini(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            file_extension = os.path.splitext(path)[1]
            if file_extension[1:] == 'csv':
                lst.append(path)
        else:
            get_list_ini(path)

lst = []
path = os.curdir
get_list_ini(path)

for item in lst:
    with open(item, 'r') as f:
        lines = f.readlines()
        if lines:
            print(item)
            print(lines)

