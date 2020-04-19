import requests


url = 'https://pcoding.ru/darkNet.php'
# content = requests.get(url).text
content = requests.get(url).content.decode('utf-8')

# f = open('content.html', 'w', encoding='utf-8')
# f.write(content)
# f.close()

with open('content.html', 'w', encoding='utf-8') as file:
	file.write(content)




# print(content)
