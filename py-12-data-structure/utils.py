def get_lines(name_file):
	f = open(name_file, 'r')
	lines = f.read().split('\n')
	f.close()
	return lines


def print_keys(name_file, step):
	with open(name_file) as lines:
		for line in lines:
			print(line)


def get_dict_keys(name_file, step):
	lines = get_lines(name_file)
	dct = {}
	while len(lines)>=step:
		dct[tuple(lines[1:step])] = lines[0]
		lines = lines[step:]
	return dct


def get_result(dict_keys, lines):
	result = ''
	for pos in range(0, len(lines[0]), 2):
		dig = [line[pos:pos+2] for line in lines]
		result += dict_keys[tuple(dig)]
	return result
