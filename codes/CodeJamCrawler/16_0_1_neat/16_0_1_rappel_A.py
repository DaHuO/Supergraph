def getDigits(n):
	d=set()
	while n>0:
		d.add(n%10)
		n=int(n//10)
	return(d)

def truncL(n):
	return int(str(n)[1:])

mI=[-1,10,45,10,23,18,15,10,12,10]
for i in range(10,10**6+1):
	mI.append(-1)
	d=set()
	n0=truncL(i)
	for j in range(1000):	
		d=d | getDigits((j+1)*i)
		if len(d)==10:
			mI[i]=j+1
			break

fin=open('A-large.in','r')
fout=open('A-large.out','w')

T=int(fin.readline())

for t in range(T):	
	N=int(fin.readline())
	m=mI[N]
	if m==-1:
		fout.write("case #%d: INSOMNIA\n" % (t+1))
	else:
		fout.write("case #%d: %d\n" % (t+1,m*N))
			
fin.close()
fout.close()