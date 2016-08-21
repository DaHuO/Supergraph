#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	Stack=list(raw_input())
	nbrflip=0
	for i in range(len(Stack)-1):
		if Stack[i+1]<>Stack[i] :
			nbrflip+=1
	if Stack[-1]=="-" :
		nbrflip+=1
	print "Case #{}: {}".format(test, nbrflip)