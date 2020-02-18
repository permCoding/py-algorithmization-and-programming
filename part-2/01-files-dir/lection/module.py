def bin_to_dec(b):
	'''
	функция перевода из 2-ой в 10-ую
	'''
	d = 0
	for i in range(len(b)):
		d += int(b[i])*2**(len(b)-1-i)
	return d

def bin_to_dec_rec(b):
	'''
	рекурсивная функция перевода из 2-ой в 10-ую
	'''
	if b == '':
		return 0
	else:
		return int(b[0])*2**(len(b)-1) + bin_to_dec_rec(b[1:])

def dec_to_bin(d):
	'''
	функция перевода из 10-й в 2-ую
	'''
	b = '1101'
	return b