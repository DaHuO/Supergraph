def dgts(di,num):
	while num>0:
		dg=int(num%10)
		if(di[dg]==0):
			di[dg]=1
		num=int(num/10)
	return di
def chkdgts(di):
	for i in range(len(di)):
		if di[i]==0:
			return False
	return True


with open('A-large.in','r') as f:
	x=int(f.readline())
	print(str(x))
	for i in range(x):
		num=int(f.readline())
		if num==0:
			print("Case #"+str(i+1)+":"+" INSOMNIA")
			continue
		d=dict()
		for j in range(10):
			d[j]=0
		k=1
		while(chkdgts(d)==False):
			d=dgts(d,k*num)
			k+=1
		print("Case #"+str(i+1)+":"+" "+str((k-1)*num))


