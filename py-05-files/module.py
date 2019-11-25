def getLines(nameFile):
	f = open(nameFile, 'r')
	text = f.read()
	lines = text.split('\n')
	return lines

# def getLines(nameFile):
# 	return open(nameFile, 'r').read().split('\n')

def palindrom(s):
	s1 = ''
	for smb in s.lower():
		if smb != ' ':
			s1 += smb
	s2 = ''
	# for i in range(len(s1)):
	# 	s2 = s1[i] + s2
	for smb in s1:
		s2 = smb + s2
	return s1 == s2