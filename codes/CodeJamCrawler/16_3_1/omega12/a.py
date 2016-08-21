import string
def solve(info):
	m=[]
	m=map(int,raw_input().split())
	s=sum(m)
	e=[]
	
	while s:
		n=m.index(max(m))
		e.append(n)
		m[n]=m[n]-1
		s=s-1
		z=b(m,-1.0)
		if len(z) >0:
			n=z[0]
			e.append(n)
			m[n]=m[n]-1
			s=s-1
		e.append(-1)
	return p(e)
def p(i):
	i.pop()
	b=[]
	for x in i:
		if x is -1:
			b.append(' ')
			continue
		b.append(string.ascii_uppercase[x])
	return ''.join(b)

def b(m,t):
	s=sum(m)
	e=[]
	for x in range(0,len(m)):
		if s is 1 and m[x] != 0:
			e.append(x)
			continue
		if (m[x])/(s-t)>=0.5:
			e.append(x)
	return e

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = input()
		print("Case #%i: %s" % (caseNr, solve(info)))
