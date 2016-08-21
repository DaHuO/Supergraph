inf = open("F_s.in","r")
out = open("F_s.out","w")

def pp(li):
	print li
	out.write(str(li[0]))
	for i in range(1,len(li)):
		out.write(" "+str(li[i]))
	out.write("\n")	

T=int(inf.readline())
for t in range(T):
	out.write("Case #"+str(t+1)+": ")
	K,C,S=map(int,inf.readline().split())
	if(K==1):
		l=[1]
		pp(l)
	else:
		if(C==1):
			if(K!=S):
				out.write("IMPOSSIBLE\n")
				print "IMPOSSIBLE"
			else:
				l=[j for j in range(1,K+1)]
				pp(l)	
		else:
			i=2
			l=[]
			#print K,i
			while((K-i)>=0):
				l.append((i-2)*K+i)
				i+=2
			i-=2	
			if(K-i==1):
				i+=1
				l.append((i-2)*K+i)	
			pp(l)	
	