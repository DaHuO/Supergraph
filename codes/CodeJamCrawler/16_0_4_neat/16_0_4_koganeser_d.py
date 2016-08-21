inp = open("in", "r")
out = open("out", "w")

inp = inp.readlines()
t = int(inp[0][:-1])
for i in range(t):
	k, c, s = map(int, inp[i + 1].split())
	out.write("Case #" + str(i + 1) + ": ")
	if s < 1 or (c == 1 and s < k):
		out.write("IMPOSSIBLE\n")
	else:
		if c == 1:
			for i in range(k):
				out.write(str(i + 1))
				if i != k - 1:
					out.write(' ')
				else:
					out.write('\n')
			continue
		if k == 1:
			out.write("1\n")
			continue
		base = (k ** c - 1) // (k - 1)
		for i in range(k):
			out.write(str(i * base + 1))
			if i != k - 1:
				out.write(' ')
			else:
				out.write('\n')
