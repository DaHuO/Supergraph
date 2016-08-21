import math

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step
def add(a):
	a.reverse()
	carry=1
	for i in range(1,len(a)-1):
		if a[i]==0:
			a[i]=1
			carry=0
			break
		else: 
			a[i]=0
			carry=1
	return a

def baseconv(num,bs,n):
	tot=0
	for i in range(n):
		tot+=num[n-1-i]*bs**i
	return tot
def prime(num):
    if (num % 2 == 0):
        return 2
    for i in mrange(3, 1000000 + 1, 2):
    	if num%i==0:
    		return i
    return 0

t=int(input())
z=input().split()
n=int(z[0])
j=int(z[1])
print("Case #1:")

num=list()
for i in range(n):
	if i==0 or i==n-1:
		num.append(1)
	else:
		num.append(0)

while(j>0):
	p=dict()
	for k in range(2,11):
		nmbr=baseconv(num,k,n)
		x=prime(nmbr)
		
		if x==0:
			num=add(num)
			num.reverse()
			break
		else: 
			p[k]=x
	if len(p)==9:
		print(''.join(map(str,num)), end=' ')
		for i in range(2,11):
			print(p[i],end=' ')
		print()
		j-=1
	num=add(num)
	num.reverse()


		






