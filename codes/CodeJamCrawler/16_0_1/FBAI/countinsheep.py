import numpy as np
import sys, getopt

found = np.empty(10)
found.fill(	False )

def check(n, count=1):
	global found

	if n==0: return -1
	n_str=str(count*n)
	#print n_str
	for i in range(len(n_str)):
		found[n_str[i]]=True
	#print found
	if np.all(found):
		return count*n
	return check(n, count+1)


#f=open(sys.argv[1])
f=sys.stdin # for pipeline usage

test_cases = int(f.readline())

for i in range(1,test_cases+1):
	found.fill(	False )
	x = int(f.readline())

	v=check(x)
	if v==-1: v='INSOMNIA'

	print 'Case #{}: {}'.format(i,v)
