
read = open('in.in', 'r')
write = open('out.out', 'w')

n = int(read.readline())

for i in range(n):
	num = int(read.readline())
	if num == 0:
		write.write('Case #{0}: INSOMNIA\n'.format(i+1))
		continue
	seen = set()
	val = 0
	while len(seen) < 10:
		val += num
		temp = val
		while temp > 0:
			seen.add(temp%10)
			temp //= 10
	write.write("Case #{0}: {1}\n".format(i+1, val))

read.close()
write.close()


