from sys import*

def permute(lvl,start):
	global L,L2,N
	global slist
	
	slist2=[]
	
	while len(slist)>1:
		for i in range(0,len(slist),2):
			if slist[i]<=slist[i+1]:
				slist2.append(slist[i]+slist[i+1])
			else:
				slist2.append(slist[i+1]+slist[i])
		slist=[h for h in slist2]
		slist2=[]

def solve():
	global N,R,P,S,L,L2
	
	pcount=0
	rcount=0
	scount=0
	
	for i in L:
		if i=="P":
			L2+="PR"
			pcount+=1
			rcount+=1
		if i=="R":
			L2+="RS"
			rcount+=1
			scount+=1
		if i=="S":
			L2+="PS"
			scount+=1
			pcount+=1
	
	L=""
	for i in L2:
		L+=i
	L2=""
	
	if scount>S or pcount>P or rcount>R:
		L=""
		return
	
	if len(L)==2**N:
		return
	else:
		solve()
		return

f=open("A-large.in","r")
g=open("output.txt","w+")
T=int(f.readline())

for i in range(1,T+1):
	[N,R,P,S]=[int(j) for j in f.readline().split()]
	
	L="P"
	L2=""
	
	solve()
	
	slist=[h for h in L]
	
	if len(L)>0:
		permute(N,0)
		g.write("Case #{}: {}\n".format(i,slist[0]))
		continue
	
	L="R"
	L2=""
	
	solve()
	
	slist=[h for h in L]
	
	if len(L)>0:
		permute(N,0)
		g.write("Case #{}: {}\n".format(i,slist[0]))
		continue
	
	L="S"
	L2=""
	
	solve()
	
	slist=[h for h in L]
	
	if len(L)>0:
		permute(N,0)
		g.write("Case #{}: {}\n".format(i,slist[0]))
		continue
	
	g.write("Case #{}: {}\n".format(i,"IMPOSSIBLE"))
	
f.close()
g.close()
