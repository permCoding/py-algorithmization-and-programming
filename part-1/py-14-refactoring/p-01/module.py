class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def __str__(self):
		return 'x = %d; y = %d' % (self.x, self.y)


class Line():
	def __init__(self, point_1, point_2):
		self.point_1 = point_1
		self.point_2 = point_2
	def __str__(self):
		return str(self.point_1) + '; ' + str(self.point_2)
	def len(self):
		kx = abs(self.point_1.x - self.point_2.x)
		ky = abs(self.point_1.y - self.point_2.y)
		return (kx**2 + ky**2)**0.5


def get_lines(name_file, title = 0):
	f = open(name_file, 'r')
	lines = [line for line in f.read().split('\n')[title:] if len(line) > 0]
	f.close()
	return lines


def get_points(lines):
	lst = []
	for line in lines:
		x, y = map(int, line.split('\t'))
		lst.append(Point(x,y))
	return lst


def get_max_point(points):
	max_point = Point()
	for point in points:
		dist_p = (point.x**2 + point.y**2)**0.5
		dist_m = (max_point.x**2 + max_point.y**2)**0.5
		if dist_p > dist_m:
			max_point = point  # Point(point.x, point.y)
	return max_point


def get_max_point_line(points):
	max_point = Point()
	max_len = 0
	for point in points:
		line = Line(Point(), point)
		if line.len() > max_len:
			max_point = point
			max_len = line.len()
	return max_point


# def get_points(lines): # прототип функции
# 	return []

# def get_max_point(points): # прототип функции
# 	return Point()
