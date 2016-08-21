inf = open("CS_l.in","r")
out = open("CS_l.out","w")
pre=open("CS_pre.in","r")
li=[0]
for line in pre:
	li.append(int(line))

T=int(inf.readline())
for t in range(T):
	out.write("Case #"+str(t+1)+": ")
	N=int(inf.readline())
	if (N==0):
		out.write("INSOMNIA\n")
	else:
		out.write(str(li[N])+"\n")	
