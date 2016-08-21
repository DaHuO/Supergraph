import sys
def rev(c):
	if c=='-':
		return '+'
	else:
		return '-'
def check(l):
	for x in range(0,len(l)):
		if l[x]=='-':
			return True
	return False
t=int(input())
for z in range(0,t):
	l=list(input())
	count=0
	while(check(l)):
		i=0;b=0
		for x in range(0,len(l)):
			if (l[-x-1]=='-'):
				i=len(l)-abs(-x-1)
				break
		if l[0]=='-':
			for x in range(0,(i+1)//2):
				b=l[i-x]
				l[i-x]=rev(l[x])
				l[x]=rev(b)
			if i%2==0:
				l[i//2]=rev(l[i//2])
			count=count+1
		else:
			for x in range(i,-1,-1):
				if l[x]=='+':
					i=x+1
					break
			for x in range(0,i//2):
				b=l[i-x-1]
				l[i-x-1]=rev(l[x])
				l[x]=rev(b)
			if i%2!=0:
				l[i//2]=rev(l[i//2])
			count=count+1
	
	print("Case #"+str(z+1)+": "+str(count))