def sheep(a):
	ans=a
	s=set([str(i) for i in range(10)])
	if a==0:
		return "INSOMNIA"
	j=1
	while s:
		ans=j*a
		for i in str(ans):
			s.discard(i)
		j+=1
	return ans
t=input()
f=open("out.txt","w")
for i in range(t):
	ans=sheep(input())
	f.write("Case #"+str(i+1)+": "+str(ans)+"\n")
f.close()
	
