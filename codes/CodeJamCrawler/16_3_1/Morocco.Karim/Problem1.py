#! /usr/bin/env python2.7

T=int(raw_input())

for test in range(1,T+1):
	N=int(raw_input())
	sens=raw_input().split()
	sens=[int(sen) for sen in sens]
	total=sum(sens)
	letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	evacplan=[]
	while total >0:
		first=""
		second=""
		m=0
		for i in range(N):
			if sens[i]> sens[m]:
				m=i
		sens[m]+=-1
		first=letters[m]
		total+=-1
		if total > 0:
			m=0
			for i in range(N):
				if sens[i]> sens[m]:
					m=i
			m2=0
			if m==0 :
				m2=1
			for i in range(N):
				if sens[i]> sens[m2] and i<>m:
					m2=i			
			if max((sens[m]-1),sens[m2])*2<= total-1:
				sens[m]+=-1
				second=letters[m]
				total+=-1
		evacplan.append(first+second)
	print "Case #{}: {}".format(test, " ".join(evacplan))
