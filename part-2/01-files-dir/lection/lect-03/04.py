import os

def get_all_files(dir, check_ext):
    for item in os.listdir(dir):
        new_path = os.path.join(dir, item)
        if os.path.isfile(new_path):
            ext = os.path.splitext(item)[1]
            if ext == check_ext:
                list_all_files.append(new_path)
        if os.path.isdir(new_path):
            get_all_files(new_path, check_ext)

list_all_files = [] # список для хранения полных путей ко всем файлам
path = os.curdir # текущая директория с программой
ext = '.ini' # выбираем расширение для поиска
get_all_files(path, ext) # запускаем рекурсию для получения списка всех файлов

# print('\n'.join(list_all_files)) # печатаем все файлы с путями

for file in list_all_files:
    print(file.split('/')[-1]) # печатаем только имена v.1
    # print(os.path.basename(file)) # печатаем только имена v.2
    # print(os.path.splitext(file)[0]) # печатаем путь + имя без расширения
    
