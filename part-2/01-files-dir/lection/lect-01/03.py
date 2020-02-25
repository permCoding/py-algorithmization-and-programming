import module3

# obj = module3.DataWork() # так по умолчанию запишется 0
obj1 = module3.DataWork(13)
obj2 = module3.DataWork()
# 13(10) => X(2) = 1101


print(obj1.num_dec)

print(obj1.dec_to_bin(10))

obj1.dec_to_bin_()
print(obj1.num_bin)

obj2.dec_to_bin_()
print(obj2.num_bin)

list_obj = [obj1, obj2, obj1]

for obj in list_obj:
    print('-', obj.num_bin)

for i in range(len(list_obj)):
    print(i+1, obj.num_bin)

for obj in list_obj:
    print(obj)