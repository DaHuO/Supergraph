import sys

		
def rev(l):
	l2 = ''
	for i in range(len(l)):
		if l[-1-i]=='+':
			l2 += '-'
		else:
			l2 += '+'
	return l2
	
def rec(l, should_be='+'):
	#print '%%%'
	#print l
	#print should_be
	if len(l)==0:
		return 0
	if (should_be=='+' and '-' not in l):
		return 0
	elif (should_be=='-' and '+' not in l):
		return 0
	else:
		rev_l = rev(l)
		t1 = rec(l[:len(l)-1], l[-1]) + (l[-1]!=should_be)
		#print t1
		t2 = rec(rev_l[:len(rev_l)-1], rev_l[-1]) + (rev_l[-1]!=should_be) + 1
		#print t2
		return min(t1,t2)

def func(k,c,s):
	c #num to check at same time
	k #num to check
	if (k+c-1)/c>s:
		return 'IMPOSSIBLE'
	
	list_k = range(k)
	list_k += [k-1]*c
	l = []
	for i in range((k+c-1)/c):
		n = 0
		for j in list_k[i*c:(i+1)*c]:
			n = (n*k) + j
		l += [n+1]
	return ' '.join([str(x) for x in l])
	
	
T = int(raw_input())
for i in range(T):
	l = raw_input()
	k,c,s = [int(x) for x in l.split()]
	print 'Case #%d: %s' % (i+1, func(k,c,s))