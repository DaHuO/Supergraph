def calcLast(x):
	digit = set()
	s = 0
	while len(digit) < 10:
		s += x
		digit |= {c for c in str(s)}
	return s

if __name__ == '__main__':
	fin = open('in.txt', 'r')
	fout = open('out.txt', 'w+')
	n = int(fin.readline())
	for i in range(n):
		x = int(fin.readline())
		fout.write('Case #{0}: {1}\n'.format(i + 1, 'INSOMNIA' if x == 0 else calcLast(x)))
	fin.close()
	fout.flush()
	fout.close()
