f1 = open('input.txt', 'r') # открываем файл для чтения
text = f1.read() # читаем все символы
print(text) # вывести все символы на экран
f1.close() # закрываем файл
print('- - - - -')


f1 = open('input.txt', 'r') # открываем файл для чтения
text = f1.read() # читаем все символы
lines = text.split('\n') # разбиваем на массив строк
f1.close() # закрываем файл


for line in lines:
	print(line) # выводим на экран все строки
print('- - - - -')


n = len(lines) # узнаём количество строк
for i in range(n):
	if i>0: # выводим часть списка
		print(lines[i]) 
print('- - - - -')


f2 = open('output.txt', 'w')
for i in range(n-1,-1,-1): # строки в обратном порядке
	line = lines[i] + '\n'
	f2.write(line) # выводим строку в файл
f2.close()


acc = 0
for line in lines:
	lst = line.split(' ')
	acc += int(lst[0]) # сумма чисел в левом столбце
print("acc =", acc)
print('- - - - -')


# создать двумерный массив
tab = [] # создали пустой список
for line in lines:
	tmp = line.split(' ') # делаем из строки список 
	tab.append(tmp) # добавляем его в tab

acc = 0
for row in range(len(tab)):
	acc += int(tab[row][0]) # строка row и столбец 0
print("acc =", acc)
print('- - - - -')

for t in tab:
	print(*t)
print('- - - - -')


for row in range(len(tab)):
	t = tab[row]
	for col in range(len(t)):
		if row==col:
			tab[row][col] = -int(tab[row][col])
for t in tab:
	print(*t)
print('- - - - -')