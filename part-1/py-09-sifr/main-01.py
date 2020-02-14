# s = 'ABC АБВГ абвг'

# for smb in s:
# 	print(smb, '\t', ord(smb))

# for i in range(32, 128):
# 	print(i, '\t', chr(i))



# наивные способы шифрования
# 1) шифрование по Цезарю
# 2) шифрование сдвигом
# 3) шифрование ^  (>> << & ^ |)

# import string
# print(string.ascii_lowercase)

z = ''
for num in range(1040, 1040+32+32):
	z += chr(num)
z += ' :;.,!-'
print(z)

s = 'Q - ПривеД, медвед!!!'
step = 3

newS = ''
for i in range(len(s)):
	pos = z.find(s[i])
	if pos == -1: # когда символа нет в строке
		newS += s[i]
	else:
		if pos + step >= len(z):
			pos = pos + step - len(z)
		else:
			pos = pos + step
		newS += z[pos]

print(s)
print(newS)










'''
лабраб 1
шифруй файлы

лабраб 2
распознать шифр
'''
