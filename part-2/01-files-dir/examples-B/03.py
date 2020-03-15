import os
import time

file_a = 'file-0.txt'

path = os.curdir  # это ссылка на текущий каталог
print(path)
path = os.getcwd()  # это полный путь к нему
print(path)
path = os.path.abspath(file_a)
print(path)

t = os.path.getctime(file_a)  # создание файла
print(t)
local_time = time.localtime(t)
print(local_time)

t = os.path.getatime(file_a)  # последнее чтение файла
print(t)
local_time = time.localtime(t) 
print(local_time)

t = os.path.getmtime(file_a)  # последняя модификация файла
print(t)
local_time = time.localtime(t)
print(local_time)
print("%d.%d.%d" % (local_time.tm_hour, local_time.tm_min, local_time.tm_sec))
print(time.strftime("%H:%M:%S %d.%m.%Y", local_time))
