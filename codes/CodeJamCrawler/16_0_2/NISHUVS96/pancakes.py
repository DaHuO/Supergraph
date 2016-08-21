import sys

T=int(input())
if T<1 or T>100:
	sys.exit(0)
	
for t in range(1,T+1):
	S=input()
	if len(S)<0 or len(S)>100:
		sys.exit(0)
		
	l=list(S)
	i=1
	count=0
	while '-' in l :
		count+=1
		while i<len(l) and l[i]==l[i-1]   :
			i+=1
		for k in range(i) :
			if l[k]=='-' :
				l[k]='+'
			else :
				l[k]='-'
	
	print("Case #"+str(t)+": "+str(count))
