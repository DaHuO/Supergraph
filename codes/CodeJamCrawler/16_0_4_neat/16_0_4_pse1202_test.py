filename = 'D-small-attempt0.in'
f = open(filename,'r')


T = int(f.readline())
for t in range(1,T+1):
	ans = ""
	K,C,S = map(int,f.readline().split())
	if K == 1:
		ans = "1"
	elif C == 1:
		if S == K:
			for i in range(1,K+1):
				ans += str(i) + " "
		else:
			ans = "IMPOSSIBLE"
	else:
		if S >= K-1:
			for i in range(2,K+1):
				ans += str(i) + " "
		else:
			ans = "IMPOSSIBLE"
	print "Case #%d: %s" % (t,ans.rstrip())