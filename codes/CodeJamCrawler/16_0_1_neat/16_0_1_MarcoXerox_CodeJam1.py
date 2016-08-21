def ans(x):
	if not x:
		return "INSOMNIA"
	s = set(range(10))
	k = 0
	while len(s):
	    k += 1
	    for v in map(int, str(x*k)):
	        s.discard(v)
	return x*k

for case in range(int(input())):
    print("Case #{0}: {1}".format(case+1, ans(int(input()))))
