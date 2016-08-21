#!/usr/bin/python
import heapq

T = int(raw_input())

def secOcc(l,i):
	count = 0
	for x in range(0,len(l)):
		if l[x] == i:
			if count == 1:
				return x
			else:
				count = count + 1


for tcounter in range(1,T+1):
	N = int(raw_input())
	P = [int(x) for x in raw_input().split()]

	total = sum(P)

	print "Case #" + str(tcounter) + ": ",
	while total:
		l = heapq.nlargest(3,P)
		#print l[0],l[1]
		i1 = P.index(l[0])
		i2 = P.index(l[1])
		if i1 == i2:
			i2 = secOcc(P,l[1])
		
		if l[0] == l[1]:

			if total > 2 and len(l) > 2 and l[2] != 0 and  (l[2] * 100.0)/(total-2) > 50:
				# we need to move them out 1 by one
				print chr(ord("A") + i1),
				P[i1] = P[i1] -1
				total = total -1
			else:
				P[i1] = P[i1]-1
				P[i2] = P[i2]-1
				print chr(ord("A") + i1) + chr(ord("A") + i2),
				total = total -2
				
		else:
			if total >2 and (l[1] * 100.0)/(total-2) > 50:
				P[i1] = P[i1]-1
				P[i2] = P[i2]-1
				print chr(ord("A") + i1) + chr(ord("A") + i2),
				total = total -2
			else:
				P[i1] = P[i1]-2
				print chr(ord("A") + i1)*2,
				total = total - 2
	
	print  
