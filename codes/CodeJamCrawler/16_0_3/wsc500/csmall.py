def isprime(x):
	for i in range(2,int(x**0.5)+1):
		if x%i==0:
			return i
	return -1

needlen=16
ans=[0]*15
cnt=0
for x in range(2**needlen):
	if len(bin(x))!=needlen+2:
		continue
	s=str(bin(x)[2:])
	if s[-1]!='1':
		continue
		
	flag=True
	for i in range(10,1,-1):
		temp=0
		for j in range(needlen):
			temp+=int(s[j])*(i**(needlen-1-j))
		key=isprime(temp)
		if (key==-1):
			flag=False
			break
		else:
			ans[i]=key
	if flag==True:
		print(s,end=" ")
		for j in range(2,11):
			print(ans[j],end=" ")
		print()
		cnt+=1
		if cnt>=50:
			exit(0)
	#print(s)
