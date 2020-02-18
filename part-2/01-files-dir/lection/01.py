

# 1101 = 13

b = input('Введите двоичное число ')
d = 0
for i in range(len(b)):
	d += int(b[i])*2**(len(b)-1-i)
print(d)