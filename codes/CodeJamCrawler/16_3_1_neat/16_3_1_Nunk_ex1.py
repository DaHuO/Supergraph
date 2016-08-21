l=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
T = int(input())


for k in range(T) :
	N=int(input())
	p=input().split(" ")
	res=""
	toSave=True
	p=list(map(int, p))
	while(toSave):
		m=max(p)
		pm=[i for i, j in enumerate(p) if j == m]
		b=not(m<=1)
		if (len(pm)==1):
			i=pm[0]
			res=res+str(l[i])+" "
			p[i]=p[i]-1
		elif (len(pm)>1 and b) or (len(pm)==2) or (len(pm)>3):
			i=pm[0]
			j=pm[1]
			res=res+str(l[i])
			p[i]=p[i]-1
			res=res+str(l[j])+" "
			p[j]=p[j]-1
		elif (len(pm)==3 and not b):
			i=pm[0]
			res=res+str(l[i])+" "
			p[i]=p[i]-1
		
		toSave=False
		for pi in p:
			if pi>0:
				toSave=True

	print('Case #'+str(k+1)+': '+str(res))

