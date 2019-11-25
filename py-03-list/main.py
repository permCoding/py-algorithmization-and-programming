import math
g = int(input("Введите в градусах - "))
x = g * math.pi / 180; q = 0.001
p = 1; f = 1; z = 1
old = x**p / f; f = 1
while True:
    p += 2; f *= p * (p-1); z = -z
    new = old + z * x**p / f
    if abs(new - old) <= q:
        break
    old = new
print(new)


'''
	continue
	break
	for in lst
	for in range
	random
	list
	string
	срезы
	_ анонимная переменная
	dec -> bin -> dec
	int bin floor ceil round
'''

# s = input()
s = '12345'
lst = [1,2,3,4,5]


# for smb in s:
#     print(smb, end='')
# print()
# for smb in lst:
#     print(smb)


# count = len(s)
# for i in range(count):
#     print(i, '\t', s[i]*2)


# for i in range(2, len(lst), 2):
#     print(i, '\t', lst[i])

# d = range(len(lst)-1, -1, -1)
# print(*d)

# for i in range(len(lst)-1, -1, -1):
#     print(i, '\t', lst[i])


# accN = 0
# for elm in lst:
#     if elm%2!=0:
#         accN += elm # acc = acc + elm
#         pass
# print('sumN =', accN)


# accP = 0
# for elm in lst:
#     if elm%2==0:
#         accP += elm # acc = acc + elm
#         pass
# print('sumP =', accP)
# print(accN-accP)


# accP, accN = 0, 0
# for elm in lst:
#     if elm%2!=0:
#         accN += elm
#     else:
#         accP += elm
# print(accN-accP)


# find = input('Введите символ - ')
# pos = 'Позиция не найдена'
# for i in range(len(s)):
#     if find == s[i]:
#         pos = i
#         break
# print(pos)


# accN = 0
# for elm in s:
#     if int(elm)%2==0:
#         continue
#     accN += int(elm)

# print(accN)


# print(*lst[0:len(lst)])
# print(lst[0:len(lst)])
# print(lst[0:len(lst):2])
# print(lst[2:])
# print(lst[0:])
# print(lst[:4])
# print(s[::-1])


# for i in range(10):
# 	print('##########')

# 1
d = range(10)
for _ in d:
	print('*')

# 2
b = input("Введите двоичное число - ")
d = int(b, 2)
print(d)
print(bin(d)[2:])
d = 0
for c in b:
	# d *= 2
	# d += int(c)
	d = d * 2 + int(c)
print(d)


'''
110 = 1*2**2 + 1*2**1 + 0*2**0 = (1*2 + 1)*2 + 0
1101 = (((1*2) + 1)*2 + 0)*2 + 1
'''

# 3
# b = b[::-1]

# d = 0
# st = 1
# for c in b:
# 	d += int(c)*st
# 	st *= 2
# print(d)






# потом побитовые операции и шифрование