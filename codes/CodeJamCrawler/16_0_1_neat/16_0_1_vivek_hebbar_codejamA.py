f = open('A-large.in','r')
o = open('out.out','w')
T = int(f.readline())
for i in range(T):
	N = int(f.readline())
	if N == 0:
		o.write("Case #"+ str(i+1) + ": INSOMNIA\n")
	else:	
		currN = N
		test = set(range(10))
		while len(test):
			test = test.difference(set([int(k) for k in str(currN)]))
			currN += N
		o.write("Case #"+ str(i+1) + ": "+ str(currN-N)+"\n")

