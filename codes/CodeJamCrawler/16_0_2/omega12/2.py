def solve(i):
	i=list(i)
	d=0
	while i and i[-1] is '+':
			i.pop()
	while i:
		z=list()
		for q in i:
			if q=='+':
				z.append('-')
			else:
				z.append('+')
		i=z
		while i:
			if i[-1]=='-':
				break
			i.pop()
		d=d+1
	return d

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = raw_input()
        print("Case #%i: %s" % (caseNr, solve(info)))
