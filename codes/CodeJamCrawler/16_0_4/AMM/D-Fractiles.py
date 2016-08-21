f=open("D-small-attempt2.in","r")
g=open("write_D_small.out","w")
content=f.read()
content=content.split('\n')
T=int(content[0])

for t in xrange(1,T+1):
	KCS=content[t]
	[K,C,S]=KCS.split(' ')
	g.write("Case #"+str(t)+": " + ' '.join([str(x) for x in range(1,int(S)+1)])+"\n")