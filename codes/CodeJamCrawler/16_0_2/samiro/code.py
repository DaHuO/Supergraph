def number_flips(string, number=0):
	if is_happy(string):
		return number
	
	number += 1
	if is_white(string):
		return number_flips(flip(string), number)
	
	first = string[0]
	for i, c in enumerate(string):
		if c != first:
			new_string = flip(string[0:i]) + string[i:len(string)]
			return number_flips(new_string, number)

def flip(string):
	res = ''
	for c in reversed(string):
		res += '-' if c == '+' else '+'
	return res

def is_happy(string):
	for c in string:
		if c=='-':
			return False
	return True

def is_white(string):
	for c in string:
		if c=='+':
			return False
	return True

input = open('B-large.in', 'r')
output = open('output.txt', 'w')
output.seek(0)
output.truncate()
T = int(input.readline())
case = 0
for i, line in enumerate(input):
	if case < T:
		flips = number_flips(string=line)
		case = case + 1
		print "Case #%d: %d" % (case, flips)
		output.write("Case #%d: %d\n" % (case, flips))
print 'Finish'
output.close()
input.close()