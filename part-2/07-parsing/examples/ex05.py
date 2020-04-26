import requests


url = 'https://tv.yandex.ru/50/channels/265'
head = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'
}
txt = requests.get(url).text
# txt = requests.get(url, headers=head).text
# txt = requests.get(url).content.decode('utf-8')[1:]

queries = {
    "time": ('<time class="channel-schedule__time">', '</time>'),
    "name": ('<span class="channel-schedule__text">', '</span>')
}

pos = 0
refs = []
limits = queries["name"]
while txt.find(limits[0], pos) >= 0:
    posLeft = txt.find(limits[0], pos) + len(limits[0])
    pos = txt.find(limits[1], posLeft)
    refs.append(txt[posLeft:pos])

print("\n".join(refs))

'''
1) написать программу, которая соберёт данные про ТВ-программы выбранного канала на текущий день
при необходимости заменить тег &quot; на обычные кавычки
и сохранит в файл текстовый в формате:
Канал
время   название программы
время   название программы
время   название программы
время   название программы
'''
