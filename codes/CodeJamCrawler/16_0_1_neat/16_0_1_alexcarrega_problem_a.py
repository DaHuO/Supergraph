import sys

f = open(sys.argv[1])
f.readline()
i = 0
for line in f:
	i = i + 1
	base_n = int(line)
	n = base_n
	visited = []
	done = [False] * 10
	j = 2
	while n not in visited and False in done:
		for digit_str in str(n):
			if digit_str >= '0' and digit_str <= '9':
				digit = int(digit_str);
				done[digit] = True
		visited.append(n)
		n = base_n * j
		j = j + 1
	sys.stdout.write('Case #' + str(i) + ': ')
	if n in visited or False in done:
		print('INSOMNIA')
	else:
		print(base_n * (j - 2))
	
	
