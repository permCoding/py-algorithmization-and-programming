#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

path = os.curdir
# print('-', path)
# path = os.getcwd()
# print('-', path)

lst_dir = os.listdir(path)
# print('\n'.join(lst_dir))
# for item in lst_dir:
#     print(item)

# for item in lst_dir:
#     if os.path.isfile(item): # isdir
#         print(item)

def check(item):
    return os.path.isfile(item)

# print('\n'.join(list(filter(lambda item: os.path.isfile(item), lst_dir))))

# print('\n'.join(list(filter(check, lst_dir))))

# def check_ext(item, ext):
#     if os.path.isfile(item):


# for item in lst_dir:
#     if os.path.isfile(item):
#         if item.split('.')[-1] == 'txt':
#             print(item)

for item in lst_dir:
    if os.path.isfile(item):
        name, ext = os.path.splitext(item)
        if ext == '.txt':
            print(name)