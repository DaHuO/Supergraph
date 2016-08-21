import math
def solve(i):
	i=i.split()
	c=list()
	for x in range(0,int(i[1])):
		t=list()
		for y in range(0,10):
			t.append(None)
		c.append(t)
	seed=(1<<(int(i[0])-1))+1
	print(seed)
	z=0
	while z<int(i[1]) and seed<(1<<(int(i[0]))):
		n=bin(seed)[2:]
		c[z][0]=n
		for x in range(2,11):
			print(str(x)+" "+n)
			q=unprime(int(n,x))
			if q==-1:
				z=z-1
				break
			else:
				c[z][x-1]=q

		seed=seed+2
		z=z+1
	for x in range(0,int(i[1])):
		c[x]=' '.join(map(str,c[x]))
	c ='\n'+'\n'.join(map(str,c))
	return c
def unprime(i):
	for x in range(2,int(math.sqrt(i))+1):
		if i%x==0:
			return x
	return -1
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        info = raw_input()
        print("Case #%i: %s" % (caseNr, solve(info)))
