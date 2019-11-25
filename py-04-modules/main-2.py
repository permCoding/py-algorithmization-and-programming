import module as m

nameFile = input('Введите имя файла - ')
lines = m.readFile(nameFile)
print(m.getSumma(lines))

