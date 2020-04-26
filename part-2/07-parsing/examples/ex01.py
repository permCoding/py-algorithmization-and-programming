import requests

# копируем содержимое страницы
url = 'https://pcoding.ru/darkNet.php'
# txt = requests.get(url).text  # так могут не совпасть кодировки
txt = requests.get(url).content.decode('utf-8')[1:]

print(txt)  # для контроля выводим на экран

# сохраняем в файл
f = open('html.txt', 'w', encoding="utf-8")
f.write(txt)
f.close()

print('сохранили страницу')

'''
оформить эти два блока в виде самостоятельных функций
get_content(url)
save_in_file(name_file)
где имя файла должно получаться автоматически
из url, например, если url = "https://pcoding.ru/darkNet.php"
то имя файла для сохранения в текущую папку "darkNet.php"
'''
