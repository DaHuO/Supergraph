def put(n,h):
	while n!=0:
		h[n%10]=1
		n=n/10
	return h
def check(h):
	for i in xrange(0,10):
		if i not in h:
			return False
	return True
def fun(n):
	h = {}
	if n==0:
		return "INSOMNIA"
	j=1
	while True:
		put(n*j,h)
		if check(h):
			return str(n*j)
		j+=1
	
f = open('A-large.in','r')
n = int(f.readline())
g = open("aaaab.txt","w")
for i in range(n):
	a = int(f.readline())
	d = fun(a)
	g.write("Case #"+str(i+1)+": "+d+"\n")
g.close()
f.close()


