T = input()
for cas in xrange(1,T+1):	
	print 'Case #'+str(cas)+":",
	K,C,S = map(int,raw_input().split())
	# print K,C,S
	xlen = K**(C-1)
	pos = 1
	for i in xrange(S):
		print pos,
		pos += xlen
	print ""


