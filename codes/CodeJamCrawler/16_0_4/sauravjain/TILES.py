import sys
for t in range(input()):
	K,C,S = map(int,raw_input().split())
	print "Case ",
	sys.stdout.write("#"),
	print t+1,
	sys.stdout.write(":"),
	if(K==1 and S>0):
		print "","1"
	elif(C==1 and S<K):
		print " IMPOSSIBLE"
	elif (C==1 and S==K):
		for i in range(1,K+1):
			print "",i,
		print
	elif(S<K-1):
		print " IMPOSSIBLE"
	else:
		for i in range(2,K+1):
			print "",i,
		print