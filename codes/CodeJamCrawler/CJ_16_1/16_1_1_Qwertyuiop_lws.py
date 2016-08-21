import sys


def build(S,L):
	if len(S)==0:
		return L
	c = S[0]
	NL = []
	for i in L:
		NL.append(c+i)
		NL.append(i+c)
	return build(S[1:],NL)

def solve(S):
	L = build(S[1:],[S[0]])
	L.sort()
	return L[-1]






f = open(sys.argv[1], "r")
F = open(sys.argv[1]+".output","w")

f.readline()
L = f.readlines()
for i in range(len(L)):
	F.write("Case #")
	F.write(str(i+1))
	F.write(": ")
	F.write(solve(L[i].rstrip()))
	F.write("\n")
F.close()
