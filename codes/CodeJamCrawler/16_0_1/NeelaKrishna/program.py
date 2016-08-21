

def digitize(N):
	digits=[]
	for i in list(str(N)):
		i=int(i)
		if i not in digits:
			digits.append(i)
	return digits

def doit(N,named):
	if N==0:
		return "INSOMNIA"
	candidate=0
	for i in range(1,1000000):
		candidate=candidate+N
		for j in digitize(candidate):
			if j not in named:
				named.append(j)
		if len(named) == 10:
			return candidate
	print "INSOMNIA"


fo=open("outputL0.out","w")
f=open("A-large.in","r")
inp=f.read()
f.close()
inp=inp.split('\n')
T=int(inp[0])
inp=inp[1:]
for x in range(T):
	N=int(inp[x])
	fo.write("Case #"+str(x+1)+": "+str(doit(N,[]))+"\n")
fo.close()