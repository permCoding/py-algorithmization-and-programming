import shutil
import os

file_a = 'file-0.txt'
file_b = 'file-2.txt'

result = ""
try:
    # shutil.copyfile(file_a, file_b)  # копирует содержимое, без атрибутов    
    shutil.copy(file_a, file_b)  # копирует с атрибутами
except PermissionError:
    result = "доступ ограничен"
else:
    result = "файл нашли и скопировали"
finally:
    print(result)


print(os.access(file_a, os.W_OK))
print(os.access(file_b, os.W_OK))
