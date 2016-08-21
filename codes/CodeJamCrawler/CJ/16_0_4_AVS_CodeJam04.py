def Fractiles(case,k,c,s):
	print ("case #{0}:".format(case),end=' ')
	if (s==k):
		for i in range(k):
			print(i+1,end=' ')
		print('')


T=int(input())
li=[]
ct=1
for i in range(T):
	li.append(str(input()))
for i in li:
	n=i.split()
	Fractiles(ct,int(n[0]),int(n[1]),int(n[2]))
	ct+=1
