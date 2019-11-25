import module as m

lines = m.getLines('input.txt')

for line in lines:
	print(m.palindrom(line), ' - ', line)