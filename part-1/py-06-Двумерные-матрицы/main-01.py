lst = [
	[1,2,3], 
	[4,5,6,4,4,4,8], 
	[7,8,9]
]

diap = range(len(lst))
for row in diap:
	for col in range(len(lst[row])):
		print(lst[row][col], '', end='')
	print()


for line in lst:
	print(*line)


import random as r

lst = []
for i in range(15):
	# diap = r.randint(1,10)
	diap = 10
	tmp = [i for i in range(diap) if i%2!=0]
	lst.append(tmp)

for line in lst:
	print(*line)

print()
lst = []
for row in range(10):
	tmp = [r.randint(1,10) for col in range(10)]
	lst.append(tmp)

for line in lst:
	print(*line)


print()
lst = []
for row in range(10):
	tmp = []
	for col in range(10):
		tmp.append(r.randint(1,10))
	lst.append(tmp)

for row in range(len(lst)):
	for col in range(len(lst[row])):
		print(lst[row][col],'\t',end='',sep='')
	print()

print()
for line in lst:
	for item in line:
		print(item,'\t',end='')
	print()

print()
for line in lst:
	print('\t'.join( map(str, line) ))

	# [2,3,4,5] => ['2','3','4','5']