#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	S=raw_input()
	letters="EFGHINORSTUVWXZ"
	letters=list(letters)
	count=[0]*len(letters)	
	for i in range(len(letters)):
		count[i]=S.count(letters[i])
	Diction=dict(zip(letters,count))
	
	repres=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
	ordr=["ZWUXGHOSFI",[0,2,4,6,8,3,1,7,5,9]]	
	numbers=[0]*10
	for i in range(10):
		c=ordr[0][i]
		nbr=Diction[c]
		numbers[ordr[1][i]]=nbr
		for cc in repres[ordr[1][i]]:
			Diction[cc]=Diction[cc]-nbr
	pnumber=""
	for i in range(10):
		for j in range(numbers[i]):
			pnumber=pnumber+str(i)
	
	print "Case #{}: {}".format(test, pnumber)
