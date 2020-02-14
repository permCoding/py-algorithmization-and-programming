from utils import get_lines

lines = get_lines('number.txt')

# используем словарь
digits  = {
	'********': '0',
	' *** * *': '1',
	'** ** **': '2',
	'** * ***': '3',
	'**** * *': '4',
	'***  ***': '5',
	' ** ****': '6',
	'** ** * ': '7',
	'**  ****': '8',
	'**** ** ': '9'
}

# используем генератор списков
result = ''
for pos in range(0, len(lines[0]), 2):
	lst = [line[pos:pos+2] for line in lines]
	key = ''.join(lst)
	result += digits[key]

print(result)
