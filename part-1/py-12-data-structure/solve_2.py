from utils import get_lines

lines = get_lines('number.txt')

# используем список - работает только для цифр
digits  = [
	'********',
	' *** * *',
	'** ** **',
	'** * ***',
	'**** * *',
	'***  ***',
	' ** ****',
	'** ** * ',
	'**  ****',
	'**** ** '
]

# используем генератор списков
result = ''
for pos in range(0, len(lines[0]), 2):
	dig = ''.join([line[pos:pos+2] for line in lines])
	result += str(digits.index(dig))

print(result)
