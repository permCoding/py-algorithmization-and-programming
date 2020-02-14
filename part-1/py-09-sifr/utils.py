def getSifr(step,s):
	newS = ''
	for smb in s:
		newS += chr(ord(smb) + step)
	return newS

def getDeSifr(step,s):
	newS = ''
	for smb in s:
		newS += chr(ord(smb) - step)
	return newS

def get(step,s,p=1): # значение по умолчанию
	newS = ''
	for smb in s:
		newS += chr(ord(smb) + p*step)
	return newS