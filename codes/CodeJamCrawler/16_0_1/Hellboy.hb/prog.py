t = int(raw_input())
k = 1
tn = set(range(10))
while k<=t:
	n = int(raw_input())
	if n == 0:
		print "Case #{}: INSOMNIA".format(k)
	else:
		bn = set([int(j) for j in str(n)])
		i = 2
		t = ""
		while len(tn-bn) > 0:
			t = str(i*n)
			bn |= set([int(j) for j in str(t)])
			i += 1
		print "Case #{}: {}".format(k,t)
	k += 1
	