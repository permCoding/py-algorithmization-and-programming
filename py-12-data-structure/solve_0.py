from utils import *


lines = get_lines('number.txt') # получим строки из файла
# for line in lines:
# 	print(line)

# smb = chr(10)
# print(smb.join(lines)) # используем join

# print(chr(10).join(lines))  # используем join

print('\n'.join(lines))  # используем join


# print_keys('keys.txt', 5)  # для контроля - печатаем ключи

# dict()
# list()
# class()
# str = '1 2 3 4'
# map(int, str.split())

t = (1,2,3,4) # tuple
print(t)
print(t[0])
for item in t:
	print(item)

# t[0] = 5 # только для списков
# print(t)