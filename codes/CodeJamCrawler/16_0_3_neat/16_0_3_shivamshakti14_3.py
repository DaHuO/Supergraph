import math

if __name__ == '__main__':
	t=int(raw_input())
	for i in range(0,t):
		inputlist=list(map(int,raw_input().split()))
		n=inputlist[0]
		#n=int(raw_input())
		stop=inputlist[1]
		stop+=1 
		#stop=int(raw_input())
		#numlis=[]
		
		finalsolution=[]

		count = 1
		for j in xrange(2**(n-2)):
			
			solutionlist = []
			s = bin(j)[2:]
			s = "0" * ((n-2)-len(s)) + s
			m=0
			x=1
			ssss=str(s)
			numlis=[]
			numlis.append(1)
			for sss in ssss:
				if sss=='0':
					numlis.append(0)
				else:
					numlis.append(1)
		

			numlis.append(1)
			for base in range(2,11):
				number=0
				for y in range(0,n):
					if numlis[y]==1:
						number += base**(n-y-1)
						
				prime=0
				for pr in range(2,int(math.sqrt(number))+1):
					if number%pr==0:
						prime =0
						solutionlist.append(pr)
						break
					else:
						prime=1
				if prime == 1:
					break
			if len(solutionlist)<9:
				del(solutionlist)
				solutionlist=[]

			if count==stop :
				break
			if prime==0:
				if count<stop and len(solutionlist)==9:
					finalsolution.append(int(str(1)+s+str(1)))
					for nn in solutionlist:
						finalsolution.append(nn)
					
					count+=1

		print 'Case #'+str(i+1)+':'
		#print finalsolution
		
		for xx in range(0,stop-1):
			print ' '.join(str(finalsolution[x]) for x in range(xx*10,xx*10+10))
		