
read = open('in.in', 'r')
write = open('out.out', 'w')

n = int(read.readline())

# each block we check in the expanded fractal can check up to 'c' blocks in the original

for case in range(n):
	line = read.readline()[:-1]
	fields = line.split(" ")
	k = int(fields[0])
	c = int(fields[1])
	s = int(fields[2])

	if c * s < k:
		write.write("Case #{0}: {1}\n".format(c+1, 'IMPOSSIBLE'))
		continue

	toCheck = []
	i = 0
	while i < k:
		total = 1
		power = 1
		for j in range(c):
			total += power * i
			power *= k
			i += 1
			if i >= k:
				break
		toCheck += [total]


	write.write("Case #{0}: {1}\n".format(case+1, " ".join(str(x) for x in toCheck)))

read.close()
write.close()


