import os,sys,math
f = open('../input.txt',"r")
output = open('../output.txt',"w")
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
T = int(f.readline())

def to10(x,b):
	s = str(x)
	d = 0
	for i in range(len(s)):
		d += int(s[i])*b**(len(s)-i-1)
	return d

def to2(x):
	return int(str(bin(x))[2:])

def div(x):
	# print(x)
	l = min(int(math.sqrt(x))+1,1000)
	# print(x)
	for i in range(2,l):
		# print(i)
		if x%i == 0:
			return i
	return 0

def divs(x):
	return [div(w) for w in [to10(x,b) for b in range(2,11)]]

def tostr(L):
	s = ""
	for l in L:
		s+=" " + str(l)
	return s[1:]

for t in range(0,T):
	N,J = [int(w) for w in f.readline().split()]
	out(t,"")
	P = 10**(N-2)
	start = to10(P,2)
	end = to10(int(str(P).replace("0","1")),2)
	for w in range(start,end+1):
		if J==0:
			break
		x = to2(w)*10+1
		L = divs(x)
		if 0 not in L:
			output.write(str(x) + " " + tostr(L)+"\n")
			J-=1