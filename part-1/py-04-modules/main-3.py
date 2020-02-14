# разбор задач из лабораторок

n = int(input())

if n>0:
	borderLeft = 1
	borderRight = n
else:
	borderLeft = n
	borderRight = 1

acc = 0
# for i in range(borderLeft, borderRight+1):
# 	acc += i # acc = acc + i

i = borderLeft
while i<borderRight+1:
	acc += i
	i += 1

print('acc =', acc)