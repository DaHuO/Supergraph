infile = open('D-small-attempt0.in', 'r')
outfile = open('fractiles_results.txt', 'w')
T = int(infile.readline())

for i in range(T):
	result = 'Case #' + str(i+1) + ':'
	K, C, S = map(int, infile.readline().strip().split())
	for j in range(K):
		result += ' ' + str(j+1)
	outfile.write(result + '\n')

infile.close()
outfile.close()