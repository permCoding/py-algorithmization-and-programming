#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	это программа демонстрирует функции перевода
	из двоичной в десятичную и обратно
	1101(2) => 13(10)
	13(10) => 1101(2)
'''
import module

b = input('Введите двоичное число ')
print(module.bin_to_dec(b))
print(module.bin_to_dec_rec(b))