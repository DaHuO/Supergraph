out = open("outa.txt", "w")

txt=open("A-large.txt","r")
S=[]

def lee(n):
	N=[]
	while n!=0:
		N.append(n%10)	
		n=n/10
	return N

def digits(k):
	n=k
	if k==0:
		return "INSOMNIA"
	else:
		A=[0 for i in range(10)]
		B=lee(k)
		for i in B:
			A[i]=1
		while A!=[1,1,1,1,1,1,1,1,1,1]:	
			k+=n
			B=lee(k)
			for i in B:
				A[i]=1
		return k


for line in txt:
	S.append(int(line))

for i in range(1,S[0]+1):
	out.write("Case #%d: %s" %(i,digits(S[i])))
	out.write("\n")
out.close()

