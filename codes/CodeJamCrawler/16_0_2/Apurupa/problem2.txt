def isallhappy(lst,n):

	for i in range(0,n):
		if lst[i]!='+':
			return 0
	return 1

def reverse(strlst,n):
	
	
	for i in range(n,-1,-1):
		
		if strlst[i]=='+':
			strlst[i]='-'
			
		elif strlst[i]=='-':
			strlst[i]='+'


def revenge(st,seq):
	no=0
	strlist=list(st)
	length=len(strlist)
	if length==1:
		if strlist[0]=='-':
			print("Case #"+str(seq)+": "+"1")
			return
		elif strlist[0]=='+':
			print("Case #"+str(seq)+": "+"0")
			return
	if isallhappy(strlist,length):
			print("Case #"+str(seq)+": "+"0")
			return
	for i in range(length-1,-1,-1):
		if isallhappy(strlist,length):
			
			print("Case #"+str(seq)+": "+str(no))
			return
		if strlist[i]=='+':
			continue
		else:
			
			reverse(strlist,i)
			no=no+1
			if isallhappy(strlist,length):
				print("Case #"+str(seq)+": "+str(no))
				return
		
			    		
		
		

n=int(input())
i=1;
while(n>0):
	inputstr=input()
	revenge(inputstr,i)
	n=n-1
	i=i+1