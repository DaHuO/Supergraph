a=[]

def getdigits(N):
	dig=0
	while N>0:
		dig=int(N%10)
		if dig not in a:
			a.append(dig)
		N=int(N/10)

T=int(input())
N=0
for i in range(T):
	N=int(input())
	temp=N
	if N==0:
		print("Case #%d: INSOMNIA"%(i+1))
	else:
		j=1
		while len(a)<10:
			temp=N*j
			getdigits(temp)
			j=j+1
		print("Case #%d: %d"%(i+1,temp))
	del a[:]
