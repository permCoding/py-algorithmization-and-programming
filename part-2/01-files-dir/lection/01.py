#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	это программа демонстрирует функции перевода
	из двоичной в десятичную и обратно
	1101(2) => 13(10)
	13(10) => 1101(2)
'''

def bin_to_dec(b):
	d = 0
	for i in range(len(b)):
		d += int(b[i])*2**(len(b)-1-i)
	return d

b = input('Введите двоичное число ')
print(bin_to_dec(b))
