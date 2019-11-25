def printN(n):
	'''
		печать всех значений
	'''
	while n>0:
		print(n)
		n -= 1


def getSummaEven(n):
	'''
		сумма четный
	'''
	acc = 0
	while n>0:
		if n%2==0:
			acc += n
		n -= 1
	return acc


z = 0
def setZ(n):
	global z
	z = n
	print(z)
	return z


import random, math
# round floor ceil


def getRandomInt(a, b):
	return math.floor(a + random.random()*(b-a+1))


def getListRnd(count, a, b):
	lst = []
	for i in range(count):
		lst.append(getRandomInt(a,b))
	return lst

###


def readFile(nameFile):
	f = open(nameFile, 'r')
	lines = f.read().split('\n')
	f.close()
	return lines


def getSumma(lines):
	acc = 0
	for line in lines:
		tmp = line.split(' ')
		for elm in tmp:
			acc += int(elm)
	return acc