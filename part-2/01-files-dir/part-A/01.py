'''
    распечатать содержимое всех папок в текущей директории
'''

import os

def print_files_in_dir(dir):
    print('dir -', dir)
    count_files = 0
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if os.path.isfile(path):
            print('file - ', path)
            count_files += 1
    print('amount: items - %d, files - %d' % (len(os.listdir(dir)), count_files))


# dir = os.getcwd()
dir = os.curdir
for item in os.listdir(dir):
    path = os.path.join(dir, item)
    # path = '\\'.join([dir, item])
    # print(path)
    if os.path.isdir(path):
        print_files_in_dir(path)

