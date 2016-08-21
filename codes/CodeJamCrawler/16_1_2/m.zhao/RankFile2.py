
read = open('in.in', 'r')
write = open('out.out', 'w')

cases = int(read.readline())

for case in range(cases):
	
	n = int(read.readline()[:-1])

	arr = [0 for _ in range(2501)]
	
	for i in range(2 * n - 1):
		line = read.readline()[:-1]
		fields = line.split(" ")
		for j in fields:
			arr[int(j)] += 1

	odd = []
	for i in range(2501):
		if arr[i] % 2 == 1:
			odd += [i]

	odd.sort()
	
	write.write("Case #{0}: {1}\n".format(case+1, " ".join(str(int(x)) for x in odd)))

read.close()
write.close()


