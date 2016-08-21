def flip(s, target = 1):
	if len(s) == 0:
		return 0
	elif s[-1] == target:
		return flip(s[:-1], target)
	else:
		return flip(s[:-1], 1 - target) + 1

if __name__ == '__main__':
	fin = open('in.txt', 'r')
	fout = open('out.txt', 'w+')
	n = int(fin.readline())
	for i in range(n):
		s = fin.readline()
		a = [0 if c == '-' else 1 for c in s]
		fout.write('Case #{0}: {1}\n'.format(i + 1, flip(a)))
	fin.close()
	fout.flush()
	fout.close()
