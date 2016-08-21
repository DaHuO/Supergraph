#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	N=int(raw_input())
	if N==0:
		print "Case #{}: {}".format(test, "INSOMNIA")
	else:
		seen=[0]*10 #list to keep track of digits seen
		M=N
		while True:				
			P=M
			while P>0:
				seen[P%10]=1
				P=P//10
			flag=1
			for b in seen:
				flag=flag*b
			if flag :
				break
			else:
				M=M+N
			
		print "Case #{}: {}".format(test, M)
