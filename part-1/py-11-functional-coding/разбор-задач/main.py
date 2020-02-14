'''
разбор задачи из ЛАБРАБ
map, filter, двумерные списки
1) вывести на экран строку с максимальной суммой чисел в строке
2) вывести на экран столбец с максимальной суммой чисел
'''

# ---1---
# f = open('input.txt', 'r')
# lines = f.read().split('\n')
# f.close()

# maxSumma = 0
# for line in lines:
# 	arr = line.split(' ')
# 	print(arr)
# 	acc = 0
# 	for item in arr:
# 		acc += int(item)
# 	if acc > maxSumma:
# 		maxSumma = acc

# print(maxSumma)


# print('- - - - - - -')
# maxSumma = 0; maxLine = ''
# for line in lines:
# 	acc = sum(list(map(int, line.split(' '))))
# 	if acc > maxSumma:
# 		maxSumma = acc
# 		maxLine = line
# print(maxLine)


# ---2---
# lst = [1,2,3,4,5]
# new = []
# for i in range(len(lst)):
# 	if lst[i]%2==0:
# 		new.append(lst[i])

# print(new)



# # item => item%2 == 0
# def jhefkjwhe(item,wew):
# 	pass
# 	return 653461
# print(*list(filter(lambda x : x%2 == 0, lst)))




# ---3---
# f = open('input2.txt', 'r')
# lines = f.read().split('\n')
# f.close()

# # tab[1][2] == 9
# # tab = [
# # 	[1,2,3,99],
# # 	[4,55,9,0],
# # 	[]
# # ]
# tab = []
# for line in lines:
# 	tab.append(list(map(int, line.split(' '))))

# for line in tab:
# 	print(line)

# height = len(tab)
# width = len(tab[0])
# # maxSum = -99999 # 1 - костыль
# # сначала сформировать список сумм по столбцам
# listSum = [] 
# for col in range(width):
# 	acc = 0
# 	for row in range(height):
# 		acc += tab[row][col]
# 	listSum.append(acc)
# print(max(listSum))


# ---4---
s = '1 2 3 4 5 6'
print(sum(list(map(int, s.split(' ')))))

def mySplit(s,sep):
	lst = []
	# for
	# while
	return lst

print(mySplit(s,sep=' '))

