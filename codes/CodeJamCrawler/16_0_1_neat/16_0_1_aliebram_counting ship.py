c =1
l=[]
t= 0
f = open('in', 'r')
fo = open('out','w')
n=int(f.readline().split()[0])
for x in range(1,n+1) :
	i=int(f.readline().split()[0])
	c=1
	l=[0,1,2,3,4,5,6,7,8,9]
	if(i==0) :
		fo.write("Case #{}: {}\n".format(x,"INSOMNIA"))
	else :
		while(1):
			t = i*c
			ns = str(t)
			for ch in ns :
				if((ord(ch)-48) in l) :
					l.remove(ord(ch)-48)
			if not l:
				break
			c+=1		
		fo.write("Case #{}: {}\n".format(x,t))
