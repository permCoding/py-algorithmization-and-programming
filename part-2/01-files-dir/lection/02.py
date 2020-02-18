#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	это программа ...
'''

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


b = input('Введите 2-ое число - ')
print(bin_to_dec(b))
