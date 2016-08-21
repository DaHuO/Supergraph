#!/usr/bin/python
N=int(raw_input())
M=N+1
for i in range (1,M):
	seq=raw_input()
	res=seq[0]
	for j in seq[1:]:
		if j< res[0]:
			res= res+j
		else:
			res =j+res
	print 'Case #%d: %s'%(i,res)
			 
	
		
	
