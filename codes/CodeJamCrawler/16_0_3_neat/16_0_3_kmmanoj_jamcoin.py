def listbin(n):
	bins=[]
	for i in range(2**(n-2)):
		bins.append("1"+binary(i,n-2)+"1")
	return bins

def binary(n,length):
	x=n
	binary=""
	for i in range(length):
		binary=str(x%2)+binary
		x//=2
	return binary

def num(binary, base):
	num=0
	for i in list(binary):
		if i=='1':
			num=num*base+1
		else:
			num=num*base
	return num

def divisor(n):
	if n==2 or n==3:
		return 0
	if n%2==0:
		return 2
	if  n%3==0:
		return 3
	
	i=5
	jump=2
	while i**2 <=n:
		if n%i==0:
			return i
		i+=jump
		jump=6-jump

	return 0

t=int(raw_input())
for i in range(t):
	[n,k]=[ int(x) for x in raw_input().split() ]
	bins=listbin(n)
	listnums={}
	for binary in bins:
		listnums[binary]=[]
		for base in range(2,11):
			listnums[binary].append(num(binary,base))		
	print "Case #"+str(i+1)+": "
	x=0
	y=0
	while x<k:
		string=bins[y]+" ";
		divs=[]
		div=0
		for z in range(2,11):
			div=divisor(listnums[bins[y]][z-2])
			if div==0:
				break;
			divs.append(div)
		if div!=0:
			for z in range(2,11):
				string+=str(divs[z-2])+" "
			print string
			x+=1
		y+=1
	
			
		
		
			
		
	

	
