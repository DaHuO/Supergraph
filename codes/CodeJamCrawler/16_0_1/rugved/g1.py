N=[]
digits=[0,1,2,3,4,5,6,7,8,9]
counter=[0,0,0,0,0,0,0,0,0,0]
T=int(input())
for i in range(T):
	temp=int(input())
	N.append(temp)
for o,j in enumerate(N):
	counter=[0,0,0,0,0,0,0,0,0,0]
	if(j==0):
		print("Case #"+str(o+1)+": INSOMNIA")
	else:
		mul=1
		while(0 in counter):
			temp=mul*j
			for ij in str(temp):
				l=int(ij)
				if(l in digits):
					counter[l]=1
			mul+=1
		print("Case #"+str(o+1)+": "+str(temp))
