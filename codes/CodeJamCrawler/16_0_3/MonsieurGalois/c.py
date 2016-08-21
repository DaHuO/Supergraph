from itertools import product
out = open("outc.txt", "w")

out.write("Case #1:"+"\n")

S=[]
for i in product('10',repeat=10):
	S.append('10000'+''.join(i)+'1')

def base(n):
	m=n[::-1]
	factors=[]
	for i in range(2,11):
		x=0
		for j in range(len(n)):
			x+=int(m[j])*(i**j)	
		factors.append(str(x))
	return factors

for i in range(500):
	k=S[i]
	out.write("%s %s" %(k+k,' '.join(base(k))))
	out.write("\n")	

out.close()

