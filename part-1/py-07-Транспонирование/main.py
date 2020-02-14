'''
txt bin csv json xml html
тест по СС
'''
f = open('input.txt', 'r')
lines = f.read().split('\n')
f.close()

tab = []
for line in lines:
	tab.append(line.split(' '))

for row in tab:
	print(*row)

for r in range(len(tab)):
	for c in range(len(tab)):
		tmp = tab[r][c]
		tab[r][c] = tab[c][r]
		tab[c][r] = tmp

# 1) заменить местами 2 переменных не используюя третью - в одну строку
# 2) сейчас прога транспонирует дважды - исправить 


for row in tab:
	print(*row)



# tab = [
# 	[1,2,3],
# 	[4,5,6],
# 	[7,8,9]
# ]
# print(tab[0][2])

# print(lines)