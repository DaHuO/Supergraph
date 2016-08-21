

out = open("output1.out", "w")
upto = 1
for inp in map(lambda x: x.strip(), open("A-large.in", "r").readlines()[1:]):
	inp = int(inp)
	digits_seen = []
	N = 1
	num = inp
	insomnia = False
	while True:
		for i in str(num):
			if i not in digits_seen:
				digits_seen.append(i)

		if len(digits_seen) == 10:
			break

		if len(str(num)) > 2*len(str(inp)) or inp == 0:
			insomnia = True
			break

		N += 1
		num = inp*N
	out.write("Case #" + str(upto) + ": ")
	if insomnia:
		out.write("INSOMNIA")
	else:
		out.write(str(num))
	out.write("\n")
	upto += 1
out.close()