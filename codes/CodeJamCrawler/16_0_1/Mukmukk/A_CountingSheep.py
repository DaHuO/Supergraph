f=open("A-large.in")

t = int(f.readline())
num=0

def szamok(i):
	if i==0:
		return i
	else:
		k=1
		digits=0
		D=[False]*10
		while digits<10:
			n=k*i
			while n!=0:
				s = n % 10
				#print s,n,digits
				if  D[s]==False:
					digits+=1
					D[s]=True
				n //= 10
			k+=1	
		return	(k-1)*i	

for k in f:
	n=int(k)
	sz=szamok(n)
	if sz!=0:
		print "Case #"+str(num+1)+":",sz
	else:
		print "Case #"+str(num+1)+": INSOMNIA"
	num+=1
		
f.close()
