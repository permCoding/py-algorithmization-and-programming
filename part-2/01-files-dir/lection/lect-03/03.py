import os

def print_dir(path):
    for item in os.listdir(path):
        if os.path.isfile(item):
            name, ext = os.path.splitext(item)
            if ext == '.txt':
                print(name)

def print_dir_all(dir, check_ext):
    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isfile(new_path):
            name, ext = os.path.splitext(item)
            if ext == check_ext:
                print(name)
        if os.path.isdir(item):
            print_dir_all(new_path, check_ext)


def get_all_files(dir, check_ext):
    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isfile(new_path):
            name, ext = os.path.splitext(item)
            if ext == check_ext:
                list_all_files.append(new_path)
        if os.path.isdir(new_path):
            get_all_files(new_path, check_ext)

list_all_files = []
path = os.curdir
ext = '.ini'
get_all_files(path, ext)

print('\n'.join(list_all_files))




# global path