def coinjam(n, j):
	v=2**(n-2)
	ans=""
	k=0
	for i in range(v):
		x=bin(i)[2:]
		temp="1"+"0"*(n-2-len(x))+x+"1"
		anst=temp+" "
		print temp, k
		for i in range(2,11):
			b=primer(int(temp,i))
			if b!=-1:
				anst+=str(b)+" "
			else:
				anst=""
				break
		if anst!="":
			ans+=anst+"\n"
			k+=1
			if k==j:
				return ans
def primer(a):
	i=3
	while i<a**0.5+1:
		if a%i==0:
			return i
		i+=2
	return -1
	
t=input()
f=open("o.txt","w")
for i in range(1,t+1):
	n,j=map(int, raw_input().split())
	f.write("Case #"+str(i)+":\n")
	f.write(coinjam(n,j))
f.close()	
