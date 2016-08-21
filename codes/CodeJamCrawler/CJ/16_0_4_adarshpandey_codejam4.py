data=open("D-small-attempt0.in","r")
S=data.read()
S=S.split("\n")
t=int(S[0])#int(input())
for i in range(1,t+1):
	s1=S[i]#input()
	k=int(s1.split()[0])
	c=int(s1.split()[1])
	s=int(s1.split()[2])
	#print("k={0} c={1} s={2}".format(k,c,s))
	if(c==1):
		if(s==k):
			s2=""
			for j in range(1,k+1):
				s2+=str(j)+" "
			print("Case #{0}: ".format(i)+s2[:-1])
		else:
			print("Case #{0}: IMPOSSIBLE".format(i))
	elif(c>1):
		if(s>=k-1):
			s2=""
			for j in range(1,k+1):
				s2+=str(j)+" "
			print("Case #{0}: ".format(i)+s2[:-1])