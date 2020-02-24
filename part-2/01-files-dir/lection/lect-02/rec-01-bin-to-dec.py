#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    1101(2) => X(10)
    1     + 1     + 0     + 1
    1*2^3 + 1 *2^2 + 0 *2^1 + 1*2^0
  ((1*2   + 1)*2   + 0)*2   + 1
    1 + 2 * get_rec()
то есть берём цифру справа и прибавляем 2, 
умноженное на оставшееся без правой цифры и
переведённое в десятичную СС    
'''

class DataProcessing():
    num_bin = '0'
    num_dec = '0'
    num_oct = '0'
    num_hex = '0'

    def __init__(self, num = '0', par = 'd'):
        if par == 'd': self.num_dec = num
        if par == 'b': self.num_bin = num
    
    def bin_to_dec(self, b):    
        return 0 if b == '' else int(b[-1]) + 2 * self.bin_to_dec(b[:-1])

    def bin_to_dec_(self):
        return self.bin_to_dec(self.num_bin)


b = '1101'
obj = DataProcessing(b)
print(obj.bin_to_dec(b))

obj.num_bin = '1000'
print(obj.bin_to_dec_())