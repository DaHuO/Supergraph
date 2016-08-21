t = int(raw_input())
def index(n,c,i):
	return i*pow(n,c-1)+1

for i in range(1,t+1):
	m = map(int, raw_input().split(" "))
	n = m[0]
	c = m[1]
	s = m[2]
	str1 = "Case #"+str(i)+": "
	L = []
	for i in range(0,n):
		L.append(index(n,c,i))
	for x in L:
		str1+=str(x)
		str1+=" "
	print str1