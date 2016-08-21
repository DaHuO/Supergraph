import os
f = open('input.txt',"r")
output = open('output.txt',"w")

#t est le numéro du cas
#sol est la solution
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
#T est le nombre de cas
T = int(f.readline())

for t in range(0,T):
	N = int(f.readline())
	a=range(0)
	i=0
	if N==0:
		out(t,"INSOMNIA")
		continue
	while len(a)!=10:
		i=(i+1)
		n=i*N
		n=str(n)
		for x in n:
			b=int(x)
			if b not in a:
				a.append(b)
		print(a)
	out(t,n)



