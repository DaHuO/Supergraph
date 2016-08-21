t=input()
for i in range(1,t+1):
	K,C,S=map(int,raw_input().split())
	index=K**(C-1)
	cnt=1
	print "Case #"+str(i)+":",
	for j in range(0,S):
		print cnt,
		cnt=cnt+index
	print " "
