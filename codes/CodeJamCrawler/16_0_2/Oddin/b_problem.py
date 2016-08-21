#!/usr/bin/python
import sys

def in_list(el,a_list):
	r=False
	for a in a_list:
		if a==el:
			r=True
			break
	return r

cases = int(sys.stdin.readline().rstrip("\n"),10)


for c in range(0,cases):
	answer=0
	cakes=[]
	for a in sys.stdin.readline().rstrip("\n"):
		cakes.append(a)

	cakes.reverse()

	while in_list('-',cakes):
		answer=answer+1
		for i in range(0,len(cakes)):
			if cakes[i]=='-':
				for j in range(i,len(cakes)):
					if cakes[j]=='-':
						cakes[j]='+'
					else:
						cakes[j]='-'
				break

			
	print("Case #"+str(c+1)+": "+str(answer))
