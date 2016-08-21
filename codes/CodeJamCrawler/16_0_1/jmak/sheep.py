infile = open('A-large.in', 'r')
outfile = open('sheep_results.txt', 'w')
T = int(infile.readline())

for i in range(T):
	result = 'Case #' + str(i+1) + ': '
	N = int(infile.readline())
	if N != 0:
		nums = set()
		j = 0
		while len(nums) < 10:
			j += 1
			for n in str(j*N):
				nums.add(n)
		result += str(j*N)
	else:
		result += 'INSOMNIA'
	outfile.write(result + '\n')

infile.close()
outfile.close()