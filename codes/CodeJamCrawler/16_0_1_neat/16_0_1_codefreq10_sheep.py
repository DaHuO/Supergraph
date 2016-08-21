t=int(raw_input())
inputList=[]
for i in range(t):
	inputList.append(int(raw_input()))
#print inputList
for i,N in enumerate(inputList):
	if N==0:
		print "Case #"+str(i+1)+': INSOMNIA'
	else:
		j=1
		d=dict()
		while(True):
			n=str(N*j)
			#print "n",n
			for digit in n:
				d[int(digit)]=1
			#print "length=",len(d.keys())
			if len(d.keys())==10:
				print "Case #"+str(i+1)+': '+str(N*j)
				break
			else:
				#N=N*j
				j+=1