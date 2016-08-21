def when_stop_counting(N):
	if N==0:
		return "INSOMNIA"
	i=0
	check=dict(zip(range(10),[0 for j in range(10)]))
	while(sum(check.values()) <10):
		i+=1
		temp=N*i
		while(temp>0):
			check[temp%10]=1
			temp/=10

	return str(N*i)

# print when_stop_counting(1)
# print when_stop_counting(2)
# print when_stop_counting(11)
# print when_stop_counting(122122121)

f=open("A-large.in","r")
g=open("write_A_large.out","w")
content=f.read()
content=content.split()
T=int(content[0])

for t in xrange(1,T+1):
	N=int(content[t])
	g.write("Case #"+str(t)+": " + when_stop_counting(N)+"\n")