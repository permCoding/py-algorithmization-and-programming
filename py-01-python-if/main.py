'''
	многострочный
	комментарий
'''

# минимальное из трёх
def getNum(x1, x2, x3):
	if x1 < x2:
		minNum = x1
	else:
		minNum = x2
	if x3 < minNum:
		minNum = x3
	return minNum

x1 = int(input("Введите первое число - "))
x2 = int(input("Введите второе число - "))
x3 = int(input("Введите третье число - "))

print("Минимальное =", getNum(x1, x2, x3))
print("Минимальное =", min(x1,x2,x3))




# num = int(input()) # float()
# print(num**.5)


############


# x = 777
# print("111111111111", "2222", x, sep="-", end="\t")
# print("222222")

# if True:
# 	pass
# 	pass
# else:
# 	pass
# 	pass 





# age = int(input('Введите возраст - '))

# if age < 18:
# 	result = "Молодой"
# else:
# 	if age > 27:
# 		result = "Спи спокойно"
# 	else:
# 		result = "Призывник"

# print(result)







# # s = input('Введите Фамилию - ')
# # s = s.capitalize()
# # print(s)
# # print(ord(s[0]))
# # n = len(s)
# # last = s[n-1].upper()
# # s = s[:n-2] + last
# # print(s)

# # lst = list(s)
# # # print(*lst)
# # lst.reverse()
# # s = ''.join(lst).capitalize()[::-1]
# # print(s)

# def main():
#   x = input()
#   y = input()
#   if x > y:
#     result = x;
#   else: 
#     result = y;
  
#   print(result)

# main()