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
	N = f.readline().replace("\n","")
	i=0
	b=0
	for i in range(0,len(N)-1):
		if N[i]!=N[i+1]:
			b=b+1
	if N[len(N)-1]=='-':
		b=b+1
	out(t,b)


