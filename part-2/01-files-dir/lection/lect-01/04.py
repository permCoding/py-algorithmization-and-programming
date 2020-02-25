import module4

obj1 = module4.WorkData(13)
obj2 = module4.WorkData()
obj3 = module4.WorkData(10)

list_obj = [obj1, obj2, obj3]

for elm in list_obj:
    print(elm.num_dec)

for elm in list_obj:
    print(elm)

for i in range(len(list_obj)):
    print(list_obj[i])


# print(obj1.num_dec)

# b = '1010'
# obj1.num_bin = b

# print(obj1.bin_to_dec(b))

# obj1.bin_to_dec_()
# print(obj1.num_dec)