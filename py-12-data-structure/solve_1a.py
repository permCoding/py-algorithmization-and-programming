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

result = ''
for pos in range(0, len(lines[0]), 2):
	key = ''
	for j in range(4): # цикл по индексам
		key += lines[j][pos:pos+2]
	result += digits[key]
print(result)
