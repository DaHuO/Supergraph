import time
F=open('output','w')
for T in range(int(input())):
	n,J=[int(x) for x in input().split()]
	S=""
	S="Case #"+str(T+1)+":"+"\n"
	def prime(n):
		for i in range(2,int(n**.5)+1):
			if n%i==0:
				return 1
		return 0
	a='1'+(n-2)*'0'+'1'
	b='1'*n
	a=int(a,2)
	b=int(b,2)
	t=[x for x in range(a,b+1) if x%2==1]
	c=0
	numbers=[2,3,5,9]
	for i in t:
		f=1
		tem=bin(i)[2:]
		values=[int(tem,j) for j in range(2,11)]
		f=1
		for j in values:
			if prime(j)==0:
				f=0
				break
		if f==1 and c<j:
			#print(tem,end=" ")
			S+=str(tem)+" "
			for j in values:
				k = 3
				while(True):
					if j%k==0:
						#print(k,end=" ")
						S+=str(k)+" "
						break
					k+=1
		if f==1:
			c+=1
			S+="\n"
		if c>=J:
			#S=S[:len(S)-1]
			print(S)
			F.write(S)
			break
F.close()
