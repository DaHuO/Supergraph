n = input()

case = 1
while case <= n:
	m = input()
	
	p = sorted([int(x), chr(ord('A')+i)] for i,x in enumerate(raw_input().split()))
	
	total = sum(n[0] for n in p)
	
	cmds = ""
	while total:
		p[-1][0] -= 1
		cmd = p[-1][1]
		total -= 1
		if p[-2][0] > total/2.:
			p[-2][0] -= 1
			total -= 1
			cmd += p[-2][1]
		
		p.sort()
		cmds += cmd+" "
	
	print "Case #"+str(case)+":", cmds
	
	case += 1