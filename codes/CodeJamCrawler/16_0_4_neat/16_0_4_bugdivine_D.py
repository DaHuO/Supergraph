t = int(raw_input())
case = 0
while t>0:
	t-=1
	case+=1
	print "Case #"+str(case)+":",

	k, c, s = map(int, raw_input().split())
	if (c==1 and s<k):
		print 'IMPOSSIBLE'
		continue
	elif (c==1):
		for a in range(1, k+1):
			print a,
	elif (c>=2 and s<(k/2+k%2)):
		print 'IMPOSSIBLE',
	elif (k==1):
		print '1',
	else:
		ans = 2
		for a in range(0, (k)/2):
			print ans,
			ans += 2*k+2
		if k%2==1:
			print ans-k-1,
	print 
