#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	S=raw_input()
	Win=S[0]
	for i in range(1,len(S)) :
		if S[i]<Win[0]:
			Win=Win+S[i]
		else:
			Win=S[i]+Win	
	print "Case #{}: {}".format(test, Win)
