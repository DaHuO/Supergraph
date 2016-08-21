import numpy as np
import sys, getopt


def check(n, count=0):
	# with this alg I do not need to flip
	if np.all(n): return count
	falsify=False
	if n[0]:
		falsify=True
	if falsify:
		for i in range(len(n)):
			if n[i]: 
				n[i]=False
			else: break
	else:
		for i in range(len(n)):
			if not n[i]: 
				n[i]=True
			else: break

	return check(n, count+1)


#f=open(sys.argv[1])
f=sys.stdin # for pipeline usage

test_cases = int(f.readline())

for i in range(1,test_cases+1):
	x = f.readline().strip()
	x=np.array([True if e=='+' else False for e in x])

	v=check(x)

	print 'Case #{}: {}'.format(i,v)
