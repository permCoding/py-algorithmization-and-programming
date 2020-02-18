
def bin_to_dec(b):
	'''
	функция перевода из 2-ой в 10-ую
	'''
	d = 0
	for i in range(len(b)):
		d += int(b[i])*2**(len(b)-1-i)
	return d
