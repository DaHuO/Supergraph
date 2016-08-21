import os,sys,copy
f = open('../input.txt',"r")
output = open('../output.txt',"w")
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
T = int(f.readline())

def deal(L,k):
	if k >= len(L):
		return 0
	for i in range(k,len(L)):
		if L[i] != L[k]:
			return 1+deal(L,i)
	return L[k]

for t in range(0,T):
	S = f.readline()
	L = []
	for s in S:
		if s == "-":
			L.append(1)
		elif s == "+":
			L.append(0)
	x = deal(L,0)
	out(t,x)