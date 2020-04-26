import requests
import shutil

def file_save_to_disk(url):
	name_file = url.split('/')[-1]
	with open(name_file, 'wb') as file:
		file.write(requests.get(url).content)


def big_save_to_disk(url):
	name_file = url.split('/')[-1]
	with requests.get(url, stream=True) as req:
		with open(name_file, 'wb') as file:
			shutil.copyfileobj(req.raw, file)
	return name_file


lst = [
	"https://pcoding.ru/ref/170.txt",
	"https://pcoding.ru/ref/171.txt"
]

for item in lst:
	# file_save_to_disk(item)
	print(big_save_to_disk(item))
