t=int(input())
k=1
while k<=t:
	s=input()
	curr=s[0]
	currS=""
	for i in s:
		if i<curr:
			currS=currS+i
		else:
			currS=i+currS
			curr=i
	print(('Case #%d: %s')%(k,currS))			
	k +=1	
