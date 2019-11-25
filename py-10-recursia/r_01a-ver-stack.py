'''
найти произведение чисел от 1 до n - факториал числа n
по умолчанию стек вызовов функций ограничен числом 1000
в Питоне есть способ увеличить величину стека
https://riptutorial.com/ru/python/example/17855/%D1%83%D0%B2%D0%B5%D0%BB%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%8B-%D1%80%D0%B5%D0%BA%D1%83%D1%80%D1%81%D0%B8%D0%B8
'''
import sys
sys.setrecursionlimit(2000)

def get(n):
	# if n <= 1:
	# 	return 1
	# else:
		return get(n - 1) * n

print(get(5))
