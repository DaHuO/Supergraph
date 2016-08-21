f = open("A-large.in")
F = open("A-large.out", "w")
case = 0
cases = 0

for line in f.readlines():
	N = int(line)
	i = 1
	sets = []
	
	if case==0:
		case += 1
		cases = int(line)
		continue
	
	if N==0:
		F.write('Case #' + str(case) + ': INSOMNIA\n')
		case += 1
		continue
	
	while len( set(sets) )!=10:
		n = N*i
		K = list(str(n))
		sets.extend(K)
		i+=1
		
	F.write('Case #' + str(case) + ': ' + str(n) + '\n')
	case += 1
	
		
