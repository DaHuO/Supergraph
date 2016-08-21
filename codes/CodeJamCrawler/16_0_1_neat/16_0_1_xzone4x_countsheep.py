def asns(n):
	if n==0:
		return("INSOMNIA")
	lst=[0]*10
	answer=n

	while(allfull(lst)==False):
		copy=answer
		while(copy!=0):
			lst[copy%10]+=1
			copy=copy//10
		answer=answer+n
	return(answer-n)


def allfull(l):
	ans=True
	for i in l:
		if i==0:
			ans=False
			break
	return ans




t=int(input())
for i in range(t):
	x=int(input())
	print ("Case #",end='')
	print (i+1,end='')
	print (": ",end='')
	print( asns(x))
