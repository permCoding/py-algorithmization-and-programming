import requests


url = 'https://pcoding.ru/darkNet.php'
txt = requests.get(url).content.decode('utf-8')[1:]

# <a href=https://pcoding.ru/ref/170.txt target=_blank>
queries = {
    "txt": ('<a href=https://pcoding.ru/ref/', ' target=_blank>')
}

pos = 0
refs = []
limits = queries["txt"]
while txt.find(limits[0], pos) >= 0:
    posLeft = txt.find(limits[0], pos) + len(limits[0])
    pos = txt.find(limits[1], posLeft)
    refs.append(txt[posLeft:pos])

print("\n".join(refs))

'''
1) написать программу, которая соберёт не названия файлов *.txt
а ссылки на эти файлы в один список и затем
все файлы из списка сохранит в текущую папку
2) оформить в виде отдельной функции куда можно передавать параметр
из какой именно папки сайта нужно сохранять файлы:
из txt, pdf, download, help, gost
'''
