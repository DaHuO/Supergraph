from math import sqrt
def is_prime(n3):
	if n3<2:
		return False;
	if n3%2==0:
		return True
	k=3
	while k*k<=n3:
		if n3%k==0:
			return True
		k+=2
	return False
for z in range(int(input())):
	y=[int(y) for y in input().split()]
	n=y[0]
	j=y[1]
	count=0
	print("Case #"+str(z+1)+":")
	l=[bin(x)[2:].rjust(n, '0') for x in range(2**n)]
	for i in range(len(l)):
		pcount=0
		if count<j:
			n1=l[i]
			o=0
			s=""
			s=s+l[i]
			if n1[0]=='1' and n1[n-1]=='1':
				for c in range(2,11):
					p=int(n1,c)
					if is_prime(p):
						pcount+=1
						for b in range(2,int(p)):
							if p%b==0:
								o=b
								break
						s=s+" "+str(o)
			if pcount==9:
				count+=1
				print(s)