import requests

# "<a href=https://pcoding.ru/ref/171.txt target=_blank>171.txt</a>"

filtres = {
	"ref": ("<a href=https://pcoding.ru/ref/", "target=_blank>")
}

url = 'https://pcoding.ru/darkNet.php'
content = requests.get(url).content.decode('utf-8')

# get_list_refs

pos = 0
limits = filtres["ref"]
while content.find(limits[0], pos) >= 0:
	posLeft = content.find(limits[0], pos) + len(limits[0])
	pos = content.find(limits[1], posLeft)
	print(content[posLeft:pos])
