c = input()

case = 1

def solveit(s, inverse):
	if not s:
		return 0
	
	if s[-1] == '+' and not inverse or s[-1] == '-' and inverse:
		return 0 + solveit(s[:-1], inverse)
	
	return 1 + solveit(s[:-1], not inverse)
	
while case <= c:
	line = raw_input()
	
	print "Case #" + str(case) +": " + str(solveit(line, False))
	
	case += 1