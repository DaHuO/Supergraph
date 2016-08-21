

def digitize(N):
	digits=[]
	for i in list(str(N)):
		i=int(i)
		if i not in digits:
			digits.append(i)
	return digits
from itertools import permutations
from collections import deque
def make(p,final):
	newfinal=[]
	for w in final:
		newfinal.append(w+p)
		newfinal.append(p+w)
	return newfinal


def doit(fw):
	final=[fw[0]]
	for p in list(fw)[1:]:
		final=make(p,final)
	return sorted(final)[-1]


fo=open("outputL0.out","w")
f=open("A-small-attempt0.in","r")
inp=f.read()
f.close()
inp=inp.split('\n')
T=int(inp[0])
inp=inp[1:]
for x in range(T):
	firstword=inp[x]
	fo.write("Case #"+str(x+1)+": "+str(doit(firstword))+"\n")
fo.close()