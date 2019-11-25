from random import randint

x = randint(100,999)
print(x)

money = 10

while True:
	y = int(input('Введите число - '))
	if x == y:
		break
	if x > y:
		print('Больше...')
	else:
		print('Меньше...')


print('-------')