import os,sys,math,copy
f = open('../input.txt',"r")
output = open('../output.txt',"w")
def out(t,sol):
	s = "Case #" + str(t+1) + ": " + str(sol)
	print(s)
	output.write(s + "\n")
T = int(f.readline())

def IsValid(P):
	if len(P)==0:
		return True
	if len(P)==1:
		return False
	if any(p[0]<0 for p in P):
		return False
	k=0
	for i in range(len(P)):
		if P[i][0]>P[k][0]:
			k=i
	return sum(P[i][0] for i in range(len(P)) if i!=k) >= P[k][0]

def IsDone(P,s):
	global solution
	if solution != "":
		return True
	if all(p[0]==0 for p in P):
		solution=s
		return True
	return False

alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
solution = ""

def step(P,s):
	if IsDone(P,s):
		return
	for i in range(len(P)):
		L=copy.deepcopy(P)
		L[i][0]-=1
		sol=s+alpha[L[i][1]]+" "
		if IsDone(L,sol):
			return
		if IsValid(L):
			step(L,sol)
	for i in range(len(P)):
		for j in range(len(L)):
			L=copy.deepcopy(P)
			L[i][0]-=1
			L[j][0]-=1
			sol=s+alpha[L[i][1]]+alpha[L[j][1]]+" "
			if IsDone(L,sol):
				return
			if IsValid(L):
				step(L,sol)

for t in range(0,T):
	N = int(f.readline())
	L = [int(w) for w in f.readline().split()]
	solution=""
	P = [[L[i],i] for i in range(len(L))]
	P.sort(key=lambda x:x[0],reverse=True)
	step(P,"")
	out(t,solution)