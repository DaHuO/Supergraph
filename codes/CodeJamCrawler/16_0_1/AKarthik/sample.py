l=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
status = False

def clearOut():
	for j in range(len(l)):
		l[j]=-1

def addToArr(d):
	if l[d] is -1:
		l[d]=d

def chkResult():
	status = True
	for j in l:
		if j is -1:
			status=False;
			break
	return status
		

fout=open('out.txt','w')

with open("A-large.in", 'r', encoding = 'utf-8') as f:
	T = int(f.readline())
	for t in range(T):
		N=int(f.readline())
		status = False
		if N is 0:
			fout.write('Case #'+str(t+1)+': INSOMNIA\n')
		else:
			clearOut()
			cycle=1
			n= N
			while(status is False):
				r=n
				while(n>0):
					d=n%10
					addToArr(int(d))
					n=int(n/10)					
				status = chkResult()
				cycle=cycle+1
				n=N*cycle
			fout.write('Case #'+str(t+1)+': '+str(r)+'\n')
fout.close()
print('done')


	
			
				
				
				
			
		
