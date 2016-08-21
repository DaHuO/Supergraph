cont = 1
T = int(raw_input())

while T > 0:
	T -= 1

	Q = (raw_input()).split()
	K, C, S = int(Q[0]), int(Q[1]), int(Q[2])

	print "Case #" + str(cont) + ":",
	cont += 1

	if C > 1:
		if K == 1:
			print "1"
		
		else:
			if S < K/2 + K % 2:
				print "IMPOSSIBLE"
		
			else:
				for i in range(K/2):
					print str(2 * i * (K + 1) + 2),
		
			if K % 2 != 0:
				print str(K),

			print
	
	else:
		if S < K:
			print "IMPOSSIBLE"
	
		else:
			for i in range(K):
				print str(i + 1),
			print