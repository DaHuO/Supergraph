import sys
b=[]
T=int(input())
if T<1 or T>100:
	sys.exit(0)
	
for i in range(1,T+1):
	N=int(input())
	if N<0 or N>10**6:
		sys.exit(0)
		
	if N==0:
		b.append("INSOMNIA")
	else:
		a=[]
		i=1
		res=0
		
		while len(a)!=10:
			num=N*i
			res=num
			i+=1
			while num!=0:
				if num%10 not in a:
					a.append(num%10)
				num=num/10
				
		if N!=0:
			b.append(res)
			
for i in range(0,T):
	print 'Case #{0}: {1}'.format(i+1,b[i])
