class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return 'x = %5d; y = %5d' % (self.x, self.y)

def get_lines(name_file, title = 0):
	f = open(name_file, 'r')
	lines = [line for line in f.read().split('\n')[title:] if len(line) > 0]
	f.close()
	return lines
