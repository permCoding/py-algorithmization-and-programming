def get(n):
	for i in range(n):
		yield i

newGenerator = get(3)
for i in newGenerator:
	print(i)