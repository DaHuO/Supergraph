def solve(n):
	LIMIT = 100 
	i = 0
	found = False
	if (n == 0):
		return "INSOMNIA"

	m = n 

	setd = set(map(int, (a for a in str(m))))
	if len(setd) == 10 : 
		found = True

	while ((i<= LIMIT) and (not found)):
		i = i+1
		m = m + n 
		news = set(map(int, (a for a in str(m))))
		setd = setd.union(news)
		if len(setd) == 10 : 
			found = True

	if (found):
		return str(m)
	else:
		return "INSOMNIA"

if __name__ == "__main__":
	# ip_fname = "a-ex.in"
	ip_fname = "A-large.in"
	# ip_fname = "A-small-attempt0.in"
	# op_fname = "a-ex.out"
	op_fname = "A-large.out"
	# op_fname = "A-small-attempt0.out"
	ip = open(ip_fname, 'r')
	op = open(op_fname , 'w')

	t = int(ip.readline())
	for tc in range(1,t+1):
		n = int(ip.readline())
		r = solve(n)
		op.write("Case #"+str(tc) + ": "+ r +"\n")
	ip.close()
	op.close()