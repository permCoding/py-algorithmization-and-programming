
'''
	циклы
	примеры перевода из двоичного в десятичное
	через номер позиции
	через скобочную форму записи
	через переворот строки
'''


'''
    Циклы
        - параметрический цикл
        - цикл с предусловием
        - цикл с постусловием
'''
# import os
# os.system('cls')

# 1
# a = int(input())
# b = int(input())

# if a > b:
#     print("Максимум -", a)
# else:
#     print("Максимум -", b)


# 2
# n = int(input("Введите число - "))

# acc = 0
# for i in range(0,n+1,1):
#     acc = acc + i

# print(acc)


# 3
# n = int(input("Введите число - "))

# acc = 0
# i = 0
# while i<=n: 
# 	acc += i
# 	i += 1 # i = i + 1

# print(acc)


# 4 - цикл с постусловием
# n = int(input("Введите число - "))

# acc = 0
# i = 0
# while True:
# 	acc += i
# 	i += 1
# 	if i>n:
# 		break

# print(acc)



# 5
# n = int(input("Введите число - "))
# mx = 16

# acc = 0
# for i in range(0,n+1,1):
# 	acc = acc + i
# 	if acc>mx:
# 		acc -= i
# 		break

# print(acc)

a = 4; b = 6; z = -6;

arr = [a, b, z]
print(min(arr))




