def bin_to_dec(b):
	'''
	b(2) => d(10)
	'''
	i = len(b) - 1
	d = 0
	for smb in b:
		d += int(smb)*2**i
		i -= 1
	return d


def bin_to_dec_rec(b):
	'''
	рекурсивная функция перевода
	b(2) => d(10)
	'''

	return 0
