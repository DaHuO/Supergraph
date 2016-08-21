def solveA(w):
	res = w[0] 
	p = w[0]

	for i in range(len(w)-1):
		j= i +1 
		nc = w[j]
		pc = res[0]

		if (ord(nc) >= ord(pc)) : 
			res = nc + res 
		else:
			res = res + nc 

	return res


if __name__ == "__main__":
	# ip_fname = "A-ex.in"
	ip_fname = "A-large.in"
	# ip_fname = "A-small-attempt0.in"
	# op_fname = "A-ex.out"
	op_fname = "A-large.out"
	# op_fname = "A-small-attempt0.out"
	ip = open(ip_fname, 'r')
	op = open(op_fname , 'w')

	t = int(ip.readline())
	for tc in range(1,t+1):
		n = ip.readline()
		r = solveA(n[:-1])
		op.write("Case #"+str(tc) + ": "+ r +"\n")
	ip.close()
	op.close()