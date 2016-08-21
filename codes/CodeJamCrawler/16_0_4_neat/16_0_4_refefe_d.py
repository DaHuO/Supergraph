import sys

T = int(sys.stdin.readline())

for k in xrange(T):
	K,C,S = map(int, sys.stdin.readline()[:-1].split(" "))
	
	if S < (K/2 + 1):
		ans = "IMPOSSIBLE"
	elif C == 1:
		if S != K:
			ans = "IMPOSSIBLE"
		else:
			ans = [i for i in xrange(1,K+1)]
			ans = " ".join(str(x) for x in ans)
	else:
		ans = [K + (K-1) * i for i in xrange((K + 1) / 2)]
		ans = " ".join(str(x) for x in ans)
	print "Case #{}: {}".format(k+1, ans)	

