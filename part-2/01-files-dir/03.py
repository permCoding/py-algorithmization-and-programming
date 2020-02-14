'''
    перебор файлов в подкаталогах
    формирование списка файлов и печать их
'''

import os

def get_list_ini(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            lst.append(path)
        else:
            get_list_ini(path)

lst = []
path = os.curdir
get_list_ini(path)
print('\n'.join(lst))