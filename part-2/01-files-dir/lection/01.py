# 1101 = 13


def bin_to_dec(b):
	d = 0
	for i in range(len(b)):
		d += int(b[i])*2**(len(b)-1-i)
	return d

b = input('Введите двоичное число ')
print(bin_to_dec(b))
