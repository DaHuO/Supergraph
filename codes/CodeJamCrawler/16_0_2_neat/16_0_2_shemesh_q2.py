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

def func(l):
	return rec(l)

	
	
T = int(raw_input())
for i in range(T):
	l = raw_input()
	print 'Case #%d: %s' % (i+1, func(l))