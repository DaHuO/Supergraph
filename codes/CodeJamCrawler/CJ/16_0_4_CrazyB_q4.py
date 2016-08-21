t=int(raw_input())
for i in xrange(t):
	k,c,s=map(int,raw_input().split())
	sol=""
	for j in range(1,k+1):
		sol=sol+str(j)+" "
	print "Case #"+str(i+1)+": "+sol
