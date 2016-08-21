t=int(input())
for i in range(1,t+1):
	n=int(input())
	l=[]
	x=1
	f=1
	while len(l)!=10:
		for d in str(x*n):
			if d not in l:
				l.append(d)
		x+=1
		if x>100:
			f=0
			break
	if f==0:
		print("Case #",i,": ","INSOMNIA",sep="")
	else:
		print("Case #",i,": ",(x-1)*n,sep="")
