#!/usr/bin/python

def check():
	for j in range(10):
		if(x.count(j)==0):
			return 1
	return 0




t = input()	#"test cases:"
tmp=0
op=[]
while(tmp<t):
	n = input()	#"picked number:"
	if n==0:
		op.append(0)
		tmp+=1
		continue
	x = map(int,str(n))
	i=1
	for j in range(100):
		if(check()):
			i+=1
			x = x + map(int,str(i*n))
		else:
			op.append(i*n)
			break
		
	tmp+=1


for i in range (t):
	if op[i]==0:
		print "Case #"+str(i+1)+": INSOMNIA"
		continue
	print "Case #"+str(i+1)+": "+str(op[i])
