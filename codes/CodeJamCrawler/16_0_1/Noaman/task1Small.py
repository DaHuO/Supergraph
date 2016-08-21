infile = open("A-large.in",'r')
out = open("output.in",'w')

test = infile.readline()

for t in range(0,int(test)):
	Num = int(infile.readline())

	if (Num == 0):
		out.write("Case #%s: INSOMNIA\n" % (t+1))
	else:
		n = 1
		seen = [False]*10
		while not (all(seen)):
			for num in str(n*Num):
				seen[int(num)] = True

			n += 1

		out.write("Case #%s: %s\n" % (t+1, (n-1)*Num))


