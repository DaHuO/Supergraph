inf = open("LW_l.in","r")
out = open("LW_l.out","w")
T=int(inf.readline())
for t in range(T):
	out.write("Case #"+str(t+1)+": ")
	S=str(inf.readline())
	li=[]
	li.append(S[0])
	for s in range(1,len(S)):
		if S[s]!='\n':
			if (S[s]>=li[0]):
				li.insert(0,S[s])
			else:
				li.append(S[s])			
	out.write(str(''.join(li))+'\n')
	print str(''.join(li))
		
