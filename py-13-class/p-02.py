f = open('points.txt', 'r')
# lines = f.readlines()
lines = [line for line in f.read().split('\n')[1:] if len(line)>0]
f.close()

print('\n'.join(lines))


# '\n' = chr(10)
# for i in range(5):
# 	print(i, chr(10), end='')

# for line in lines:
# 	print(ord(line[len(line)-1]))
