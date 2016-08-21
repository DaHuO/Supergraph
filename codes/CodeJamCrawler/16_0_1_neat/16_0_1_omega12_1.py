def solve(info):
	if info ==0:
		return 'INSOMNIA'
	z=info
	c=[0,0,0,0,0,0,0,0,0,0]
	d=1;
	while sum(c) !=10:
		info=map(int,str(info))
		for i in info:
			c[i]=1
		while info and info[-1] is 0:
			info.pop()
		d=d+1
		info=z*d
	return info-z

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = input()
        print("Case #%i: %s" % (caseNr, solve(info)))
