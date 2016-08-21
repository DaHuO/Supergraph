T = int(input())
for t in range(T):
	K, C, S = [int(i) for i in input().split(' ')]
	#if C == 1:
	#	output = [str(k+1) for k in range(K)]
	#else:
	#output = [str(c*(K**(C - 1)) + c + 1) for c in range(K)]
	output = [i*sum([K**j for j in range(C)]) + 1 for i in range(K)]
	print("Case #%s: %s" % (t + 1, ' '.join([str(s) for s in output])))