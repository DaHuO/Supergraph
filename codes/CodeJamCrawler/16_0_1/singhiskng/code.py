def p(n):
	c = [0]*10
	i = 1
	found = False
	while not found:
		nn = str(n*i)
		for j in nn:
			c[int(j)] = 1
		if all(c):
			found = True
			return n*i
		i+=1

T = input()

for x in range(1,T+1):
	N = input()
	if N==0:
		print "Case #"+ str(x) + ": " + "INSOMNIA"
	else:
		print "Case #"+ str(x) + ": " + str(p(N));
