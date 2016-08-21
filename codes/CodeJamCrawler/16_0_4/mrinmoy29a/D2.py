f = open("D-small-attempt1.in")
F = open("D-small-attempt1.out", "w")
case = 0
cases = 0

for line in f.readlines():
	if case==0:
		case += 1
		cases = int(line)
		continue
	
	k, c, s = ( int(i) for i in line.split(' '))
	F.write('Case #' + str(case) + ':')
	
	if k-c+1 > s:
		F.write(' IMPOSSIBLE\n')
		case += 1
		continue
	
	if(k-c+1)<=0:
		c=k
	
	
	numbers = []
	mul = 1

		
	for i in xrange(s):
		numbers.append(mul)
		mul += 1
	
	for number in numbers:
		F.write( ' ' + str(number))
	F.write('\n')
	
	case += 1

f.close()
F.close()
		
		
