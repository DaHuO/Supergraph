import sys
t=int(input())
for z in range(0,t):
	n=list(input())
	s=n[0]
	for x in range(1,len(n)):
		if n[x]>=s[0]:
			s=n[x]+s
		else:
			s=s+n[x]
	sys.stdout=open('out.txt','a')
	print('Case #'+str(z+1)+': '+s)