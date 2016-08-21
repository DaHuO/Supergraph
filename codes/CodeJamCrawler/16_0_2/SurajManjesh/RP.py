inf = open("RP_l.in","r")
out = open("RP_l.out","w")
T=int(inf.readline())
for t in range(T):
	out.write("Case #"+str(t+1)+": ")
	li=list(inf.readline())
	if '\n' in li:
		li.remove('\n')
	count=0	
	for l in range(len(li)-1):
		if(li[l]!=li[l+1]):
			count+=1
	if (li[-1]=='-'):
		count+=1		
	print count	
	out.write(str(count)+"\n")	
