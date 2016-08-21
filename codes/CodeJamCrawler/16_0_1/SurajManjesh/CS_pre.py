pre=open("CS_pre.in","w")
N=1
while (N<=1e6):
	i=1
	li=[]
	while(sum(li)!=45 or len(li)!=10):
		arr=map(int,list(str(i*N)))
		#print arr
		i+=1
		for a in arr:
			if a not in li:
				li.append(a) 
		#print li,i		
	pre.write(str((i-1)*N)+"\n")	
	N+=1		
pre.close()	