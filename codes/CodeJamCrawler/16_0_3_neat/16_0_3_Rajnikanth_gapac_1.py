def is_prime(x):
	for i in xrange(2,int(x**0.5) + 100):
		if (x % i) == 0:
			print i,
			break
x = open("out_d.txt")
temp = []
for i in x.readlines():
    temp += [int(i)]
for i in xrange(50):
    xx = bin(temp[i])[2:]
    print xx,
    for j in xrange(2,11):
        is_prime(int(xx,j))
    print
