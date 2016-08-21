def solve(fileName):
	solutions = []
	with open(fileName, 'rb') as f:
		n = int(f.readline())
		for i in range(n):
			a = map(int, f.readline().split())
			solutions.append(' '.join(map(str, range(1, a[0] + 1))))
	with open('answer.txt', 'wb') as f:
		for i in range(len(solutions)):
			f.write(('Case #%d: ' % (i + 1)) + solutions[i] + '\n')
