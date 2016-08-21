def main():
	file_name = 'q4.in'
	f = open(file_name , 'r')
	lines = f.read().splitlines()
	test_cases = int(lines[0])
	result = ''
	for i in xrange(1, test_cases + 1):
		line = lines[i]
		sp = line.split()
		K, C, S = int(sp[0]), int(sp[1]), int(sp[2])
		last = pow(K,C)
		size = pow(K,C-1)
		checks = ''
		for j in xrange(S):
			checks += str((j+1) * size) + ' '
		r = "Case #" + str(i) + ": " + checks[:-1] + '\n'
		result += r
	print result
	f = open('q4.out', 'w')
	f.write(result)
	f.close()
if __name__ == '__main__':
	main()
