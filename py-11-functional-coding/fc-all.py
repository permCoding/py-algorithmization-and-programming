from operator import itemgetter, attrgetter

# анонимные функции
def acc_1(a, b):
	return a + b

acc_2 = lambda a, b: a + b

getMax = lambda a, b: a if a>b else b

a = 5; b = 3
print(acc_1(a, b))
print(acc_2(a, b))
print(getMax(a, b))


# генератор списка
lst = [i for i in range(10)]
print(*lst)
# print(','.join(lst))  # не работает
print(','.join(map(str, lst)))  # а так работает


lst = [i**2 for i in range(10)]
print(*lst)


step2 = lambda x : x**2
lst = [step2(i) for i in range(10)]
print(*lst)


def _step2(x): return x**2
lst = [_step2(i) for i in range(10)]
print(*lst)


# map
lst = [1, 2, 3, 4, 5]
lst = map(str, lst)
print(*lst)

lst = [1, 2, 3, 4, 5]
lst = list(map(str, lst))
print(lst)

lst = [1, 2, 3, 4, 5]
lst = list(map(lambda x: x % 2 != 0, lst))
print(lst)

lst = [1, 2, 3, 4, 5]
lst = list(map(lambda x: 1 if x % 2 != 0 else 0, lst))
print(lst)

# filter
lst = [1, 2, 3, 4, 5]
lst = list(filter(lambda x: x % 2 != 0, lst))
print(lst)

lst = [1, 2, 3, 4, 5]
print(sum(list(filter(lambda x: x % 2 != 0, lst))))

# reduce
from functools import reduce

lst = [1, 2, 3, 4, 5]
print(reduce(lambda a,b: a + b, lst))

lst = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, lst, 100))

lst = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + (b if b % 2 != 0 else 0), lst))

# zip
ages = [22, 21, 17, 18]
names = ['AA', 'BB', 'CC', 'DD']
lst = list(zip(names, ages))

for item in lst:
	print(item[0], item[1])


# отсортируем по возрасту - ver.1 - sort + список списков
lst.sort(key=lambda elm: elm[1])
for item in lst:
	print(item[0], item[1])


# отсортируем по возрасту - ver.2 - class
ages = [22, 21, 17, 18]
names = ['AA', 'BB', 'CC', 'DD']
lst = list(zip(names, ages))

class Student():
	def __init__(self, age, name):
		self.age = age
		self.name = name

students = []
for item in lst:
	students.append(Student(item[0], item[1]))

# students.sort(key=lambda item: item.name)
students.sort(key=attrgetter('name'),reverse=True)
for item in students:
	print('-', item.age, item.name)


# отсортируем по возрасту - ver.3 - sorted
ages = [22, 21, 17, 18]
names = ['AA', 'BB', 'CC', 'DD']
lst = list(zip(names, ages))

print(*sorted(ages))
print(*sorted(lst, key=lambda x: x[1]))
print(*sorted(lst, key=lambda x: x[1], reverse=True))
print(*sorted(lst, key=itemgetter(1), reverse=True))


# отсортируем по возрасту - ver.4 - вручную - нет смысла, но...
ages = [22, 21, 17, 18]
names = ['AA', 'BB', 'CC', 'DD']
lst = list(zip(names, ages))
#
#
#
#
