t=long(raw_input())
x=t
ans=[]


import sys


	
def calc(num,mp,i):

	a=[]
	while mp!=10:
		fx=num*i
		fx=str(fx)
		
		for p in range(0,len(fx)):

			a.append(int(fx[p]))
		cc=0
		for m in range(0,10):
			if a.count(m)>0:
				cc+=1
		mp=cc
		i=i+1
	return fx


	
while t>0:
	n=long(raw_input())
	if n==0:
		ans.append('INSOMNIA')
	else:
		m=calc(n,0,1)
	
		ans.append(m)
	t=t-1
for out in range(1,x+1):
	sys.stdout.write('Case #')
	print out,
	sys.stdout.write(': ')
	print (ans[out-1])
	


