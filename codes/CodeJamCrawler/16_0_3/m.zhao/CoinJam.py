
read = open('in.in', 'r')
write = open('out.out', 'w')

cases = int(read.readline())

# odd bases are obvious
# even bases can be considered in mode b+1, then easy

for case in range(cases):
	write.write("Case #{0}:\n".format(case+1))
	
	line = read.readline()[:-1]
	fields = line.split(" ")
	n = int(fields[0])
	j = int(fields[1])

	odd1 = 1
	odd2 = 3
	even1 = 2
	even2 = 4
	for i in range(j):
		num = [0 for _ in range(n)]
		num[0] = 1
		num[-1] = 1
		num[odd1] = 1
		num[odd2] = 1
		num[even1] = 1
		num[even2] = 1
		write.write("{0} 3 2 5 2 7 2 9 2 11\n".format("".join(str(x) for x in num)))
		even2 += 2
		if even2 >= n:
			even1 += 2
			if even1 >= n - 2:
				odd2 += 2
				if odd2 > n - 1:
					odd1 += 2
					odd2 = odd1 + 2
				even1 = 2
			even2 = even1 + 2


read.close()
write.close()


