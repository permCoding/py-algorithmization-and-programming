from utils import *


dict_keys = get_dict_keys('keys.txt', 5) # получим словарь ключей
# print(keys)


lines = get_lines('number.txt') # получим строки из файла


result = get_result(dict_keys, lines)  # декодируем запись


print('result =', result) # печатаем результат
