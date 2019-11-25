'''
	циклы файлы строки функции модули списки
	random
'''


# 1
# from module import printN, getSummaEven
# n = int(input('Введите число - '))
# printN(n)
# acc = getSummaEven(n)
# print('Сумма', n,' =', acc)


# 2
# import module as m
# print(m.setZ(9))
# print(m.z)



# 3
import module as m

# a = 3; b = 5
# print( m.getRandomInt(a, b) )


# 4
lst = m.getListRnd(10, 1, 5)
print(lst)
print(*lst)
for elm in lst:
	print(elm)





# import math

# n = 16


# z = math.log2(n)
# if z * 10 // 10 == z:
# 	print("YES")
# else:
# 	print("NO")
# print("YES" if z*10//10==z else "NO")



# tmp = n
# while tmp>1:
# 	tmp /= 2
# print("YES" if tmp==1 else "NO")



# acc = 0
# while n>0:
# 	n >>= 1
# 	acc += n & 1
# print("YES" if acc==1 else "NO")
