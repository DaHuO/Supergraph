def sleep_sheep(N):
	if N == 0:
		return "INSOMNIA"
	a, z = range(10), 1
	while(True):
		x = N * z
		t = [q for q in a if q  not in [int(j) for j in str(x)]]
		if len(t) < 1:
			break
		else:
			z += 1
			a = t
	return x

f = open("A-large.in").read().split("\n")[:-1]
o = open("small.out", "w")
for i in range(1,101):
	o.write("Case #"+str(i)+": "+str(sleep_sheep(int(f[i])))+"\n")

