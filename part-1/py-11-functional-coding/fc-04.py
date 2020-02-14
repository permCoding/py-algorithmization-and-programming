# zip
s1 = '18 22 21 21 19'
ages = list(map(int, s1.split()))

s2 = 'AAA BBB CCC DDD EEE FFF'
names = s2.split()

print(ages)
print(names)
students = [
	('AAA',18),
	('BBB',22)
]
students = list(zip(names, ages))
print(students)

for student in students:
	print(student)

for student in students: # обычный вывод
	print('имя - ', student[0], ', возраст - ', student[1], sep='')

for student in students: # форматированный вывод
	print('имя - %s, возраст - %d' % (student[0], student[1]))
