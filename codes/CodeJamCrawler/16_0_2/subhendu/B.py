def solve(n):
	res  = -1
	stack = [c for c in n]

	if (n.find("-") == -1 ) :
		res = res + 1
	else:
		l = 0 
		sol = []
		for i in range(len(stack)):
			l = l+1
			if ((i>0) and  (stack[i-1] == stack[i])):
				l = l-1
			if (stack[i] == '-'):
				if ((i>0) and  (stack[i-1] == -1)):
					sol.append(sol[i-1])
				else:
					sol.append(l)
			else:
				sol.append(0)
		res = max(sol)
	return res

if __name__ == "__main__":
	ip_fname = "B-large.in"
	# ip_fname = "B-small-attempt0.in"
	op_fname = "B-large.out"
	# op_fname = "B-small-attempt0.out"
	ip = open(ip_fname, 'r')
	op = open(op_fname , 'w')

	t = int(ip.readline())
	for tc in range(1,t+1):
		n = ip.readline()
		r = solve(n.strip())
		op.write("Case #"+str(tc) + ": "+ str(r) +"\n")
	ip.close()
	op.close()