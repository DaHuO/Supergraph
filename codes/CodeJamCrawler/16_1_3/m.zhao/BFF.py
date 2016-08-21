
read = open('in.in', 'r')
write = open('out.out', 'w')

cases = int(read.readline())

for case in range(cases):
	
	n = int(read.readline()[:-1])
	line = read.readline()[:-1]
	fields = line.split(" ")
	bffs = [int(x) - 1 for x in fields]
	d = {}
	for i in range(len(bffs)):
		if bffs[bffs[i]] == i:
			d[i] = 1

	maxCycle = 0
	for i in range(len(bffs)):
		if i in d:
			continue
		length = 1
		cur = i
		prev = -1
		while bffs[cur] != i and bffs[cur] != prev and length <= len(bffs):
			# print(i, bffs[cur], cur, prev)
			prev = cur
			cur = bffs[cur]
			length += 1
		if length > len(bffs):
			continue
		if bffs[cur] == i:
			maxCycle = max(maxCycle, length)
		else:
			d[cur] = max(d[cur], length - 1)

	sumd = 0
	for k in d:
		sumd += d[k]

	print(max(sumd, maxCycle))


	
	write.write("Case #{0}: {1}\n".format(case+1, max(sumd, maxCycle)))

read.close()
write.close()


