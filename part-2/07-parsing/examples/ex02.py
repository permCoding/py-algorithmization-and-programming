import requests

url = 'https://pcoding.ru/darkNet.php'

with requests.get(url) as req: # alias - псевдоним
    txt = req.content.decode('utf-8')[1:]
    print(txt)
    with open('html.txt', 'w', encoding="utf-8") as file:
        file.write(txt)
