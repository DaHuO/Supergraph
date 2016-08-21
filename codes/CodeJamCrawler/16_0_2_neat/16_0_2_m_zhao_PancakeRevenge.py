
read = open('in.in', 'r')
write = open('out.out', 'w')

n = int(read.readline())

for c in range(n):
	
	line = read.readline()
	reverses = 0
	cur = line[0]
	for i in range(0, len(line) - 1):
		if cur != line[i]:
			reverses += 1
			cur = line[i]
	if cur == '-':
		reverses += 1
	
	write.write("Case #{0}: {1}\n".format(c+1, reverses))

read.close()
write.close()


