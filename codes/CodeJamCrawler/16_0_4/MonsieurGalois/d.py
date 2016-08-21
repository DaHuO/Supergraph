out = open("outd.txt", "w")


txt=open("data.txt","r")
S=[]
for line in txt:
	x=line.split()
	x=map(int,x)
	S.append(x)

n=S[0][0]

for i in range(1,1+n):
	m="Case #%d: " %(i)
	n=' '.join(map(str,range(1,S[i][0]+1)))
	out.write(m+n+'\n')

out.close()
