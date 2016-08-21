with open("A-large.in") as infile:
	lines = [int(item) for item in infile.readlines()]
	ntests = lines[0]
	numbers = lines[1:]
# ntests = input()
outfile = open("Output.txt", 'w')
for case in range(ntests):
	# n = input()
	n = numbers[case]
	seen = [0]*10
	seen_sum = 0
	i = 1
	if n == 0:
		outfile.write("Case #{}: INSOMNIA\n".format(case+1))
		continue
	else:
		num = n
		while seen_sum != 10:
			n = num*i
			orginal_num = n
			while n:
				digit = n % 10
				if seen[digit] == 0:
					seen[digit] = 1
					seen_sum += 1
					if seen_sum == 10: 
						outfile.write("Case #{}: {}\n".format(case + 1, orginal_num))
						break
				n = n / 10
			i = i + 1
		
