import os,sys
f = open('../input.txt',"r")
output = open('../output.txt',"w")
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
T = int(f.readline())

for t in range(0,T):
	N = int(f.readline())
	done = [False for i in range(10)]
	x = 0
	i = 1
	if N != 0:
		while False in done and i < 100000:
			x = i*N
			i+=1
			s = str(x)
			for j in range(len(s)):
				done[int(s[j])] = True
		w = str(x)
	else:
		w="INSOMNIA"
	out(t,w)