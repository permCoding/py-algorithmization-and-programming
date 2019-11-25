# анонимные функции, объекты, сортировка, генератор списка
# ООП рефакторинг


class Student():
	def __init__(self, id, name, age, ball):
		self.id = int(id)
		self.name = name
		self.age = int(age)
		self.ball = float(ball)

	def __repr__(self):
		# return self.name + '\t' + str(self.age) + '\t' + str(self.ball)
		# return '{0}\t{1}\t{2}'.format(self.name, self.age, self.ball)
		return '%20s%9d%9.2f' % (self.name, self.age, self.ball)


f = open('students.txt', 'r')
lines = f.read().split('\n')
f.close()


students = []
for line in lines[1:]:
	id,name,age,ball = line.split('\t')
	students.append(Student(id, name, age, ball))


students.sort(key = lambda item: item.age, reverse = True)
for item in students:
	# print('-', item.age, '-', item.name)
	print(item)


