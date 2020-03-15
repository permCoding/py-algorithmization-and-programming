import shutil
import os

file_a = 'file-0.txt'
file_b = 'file-1.txt'

result = ""
try:
    shutil.copyfile(file_a, file_b)
except FileNotFoundError:
    result = "нет файла в директории"
except IsADirectoryError:
    result = "это не файл, это директория"
except PermissionError:
    result = "доступ ограничен"
else:
    result = "файл нашли и скопировали его содержимое"
finally:
    print(result)


print(os.access(file_a, os.F_OK))
print(os.access(file_a, os.R_OK))
print(os.access(file_a, os.W_OK))
print(os.access(file_b, os.F_OK))
print(os.access(file_b, os.R_OK))
print(os.access(file_b, os.W_OK))
os.chmod(file_b, 0o444)
# os.chmod(file_b, 0o666)
print(os.access(file_b, os.R_OK))
print(os.access(file_b, os.W_OK))
