def countplus(A):
	if A.count('+') == len(A):	return 0
	for i in xrange(len(A)):
		if A[i] == '+':
			A[i] = '-'
		else:
			return countminus(A) + 1
def countminus(A):
	if A.count('-') == len(A): return 1
	for i in xrange(len(A)):
		if A[i] == '-':
			A[i] = '+'
		else:
			return countplus(A) + 1
def countNums(A):
	if A.count('-') == len(A):	return 1
	if A.count('+') == len(A):	return 0
	if A[0] == '+':	return countplus(A)
	else:	return countminus(A)
for tc in xrange(int(raw_input())):
	S = raw_input()
	s = list(S)
	print "Case #%d: %d" %(tc+1, countNums(s))
