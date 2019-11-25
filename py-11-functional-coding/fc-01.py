def summa(a,b):
	'''
	функция
	поиска суммы двух аргументов
	'''
	return a + b

func = lambda a, b : a + b # анонимная функция

x = 2; y = 6
print(summa(x,y))
print(func(x,y))

s = '1 2 3 4 5'
# обычный подход
lst = s.split()
print(lst)
acc = 0
for item in lst:
	acc += int(item)
print(acc)

# функциональный подход
print(sum(map(int, s.split())))
print(map(int, s.split()))
for item in map(int, s.split()):
	print(item)
print(list(map(int, s.split())))
print(*list(map(int, s.split())))





def getInt(arg): # традиционный подход
	return int(arg)

print(sum(map(getInt, s.split())))

# функциональный поход
print(sum(map(lambda arg: int(arg), s.split())))
