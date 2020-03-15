import requests  # импортируем модуль
import shutil
import requests


def download_file(url):
    name_file = url.split('/')[-1]
    with open(name_file, 'wb') as file:
        data = requests.get(url)
        file.write(data.content)
    return name_file


def download_file_big(url):
    name_file = url.split('/')[-1]
    with requests.get(url, stream=True) as req:
        with open(name_file, 'wb') as file:
            shutil.copyfileobj(req.raw, file)
    return name_file


url = "https://pcoding.ru/darkNet.php"
print('сохранили файл -', download_file(url))


# url = "https://pcoding.ru/ref/191.txt"
# print('сохранили файл -', download_file(url))
# url = "https://pcoding.ru/pdf/PythonJunior.pdf"
# print('сохранили файл -', download_file_big(url))

