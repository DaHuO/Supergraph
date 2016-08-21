# your code goes here
import itertools,math
def isprime(n):
	if n==1:return 0
	for  i in range(2,int(math.sqrt(n))+1):
		if(n%i==0):
			return 0
	return 1
def arr():
	for x in range(1,11):
		for y in range(0,32):
			l.append(x**y)
l=[]
arr()			
t=int(input())
for d in range(t):
	n,k=map(int,input().split())
	b,count,c=[],0,[]
	for p in itertools.product("10",repeat=n):
		flag,a=0,[]
		for j in range(2,11):
			sum,flag=0,0
			if(p[0]=='1' and p[n-1]=='1'):
				for i in range(0,n):
					sum+=int(p[i])*l[32*(j-1)+n-i-1]
				a.append(sum)
			if(isprime(int(sum))):
				flag=1
				break
		if(not flag and count<k):
			count+=1
			b.append(a)
			c.append(p)
			# print(a)
		if(count==k):
			break
	print('{0}{1}{2}'.format("Case #",d+1,":"))
	for j in range(k):
		s=str()
		for g in range(n):
			s+=c[j][g]
		print(s,end=" ")
		for i in range(9):
			for r in range(2,b[j][i]//2):
				if(b[j][i]%r==0):
					print (r,end=" ")
					break
		print()		