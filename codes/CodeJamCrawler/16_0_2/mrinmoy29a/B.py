f = open("B-large.in", "r")
F = open("B-large.out", "w")
case = 0
cases = 0

for line in f.readlines():
	attempts = 0
	
	if case==0:
		case += 1
		cases = int(line)
		continue
	
	L = line.strip('\n')
	prev = '*'
	
	for symbol in L:
		if symbol!=prev:
			prev = symbol
			attempts += 1
	
	if L[-1]=='+':
		attempts -= 1
		
	F.write('Case #' + str(case) + ': ' + str(attempts) + '\n')
	case += 1
	
f.close()
F.close()
