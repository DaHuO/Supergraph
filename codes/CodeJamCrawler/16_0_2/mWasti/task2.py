def flip(char):
	if char == '+':
		return '-'
	elif char == '-':
		return '+'
	else:
		return null

def flipall(string):
	string = list(string)
	for i in range(0,len(string)):
		string[i] = flip(string[i])
	return "".join(string)

def checkplus(string):
	for ch in string:
		if ch == '-':
			return False
	return True

def checkminus(string):
	for ch in string:
		if ch == '+':
			return False
	return True

def parse(string):
	for i in range(0,len(string)-1):
		if string[i] == '-' and string[i+1] == '+':
			return i+1
		elif string[i] == '+' and string[i+1] == '-':
			return i+1
	return -1

def flipmain(string, counter):
	if checkplus(string):
		return counter

	if checkminus(string):
		return counter+1

	checkindex = parse(string)
	string = flipall(string[:checkindex])+ string[checkindex:]
	counter = flipmain(string, counter+1)
	return counter

file = open('B-large.in')
num_of_cases = int(file.readline())
output_file = open('output1.txt', 'w')

for case in range(1,num_of_cases+1):
	string = file.readline().strip()
	counter = flipmain(string, 0)
	
	print >> output_file, "Case #%d: %s" % (case, counter)
