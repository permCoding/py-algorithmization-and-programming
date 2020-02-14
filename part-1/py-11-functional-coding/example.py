'''
map filter reduce
list set dict
'''
from functools import reduce

lst = [1,2,3,4,5]
m = reduce(lambda a,b : a+b, lst)

print(m)

a = [1,2,3]
b = ["aaa","bbb","ccc"]

allList = list(zip(a,b))

print(*allList)

for item in allList:
	d = item[1].rjust(10,' ')
	print(item[0],d)
	# print(item[0] + item[1].rjust(12, " ")


