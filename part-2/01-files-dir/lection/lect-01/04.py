import module4

obj = module4.WorkData(13)

print(obj.num_dec)

b = '1010'
obj.num_bin = b

print(obj.bin_to_dec(b))

obj.bin_to_dec_()
print(obj.num_dec)