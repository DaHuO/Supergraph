def clean(k, c, s):
	if s * c < k:
		return []
	res = []
	pos = 0
	finish = False
	for i in range(s):
		num = 0
		for j in range(c):
			num *= k
			num += pos
			pos += 1
			if pos == k:
				pos = 0
				finish = True
		res += [num + 1]
		if finish:
			break
	return res

if __name__ == '__main__':
	fin = open('in.txt', 'r')
	fout = open('out.txt', 'w+')
	n = int(fin.readline())
	for i in range(n):
		line = fin.readline()
		k, c, s = [int(x) for x in line.split(' ')]
		fout.write('Case #{0}:'.format(i + 1))
		res = clean(k, c, s)
		if len(res) == 0:
			fout.write(' IMPOSSIBLE')
		else:
			for tile in clean(k, c, s):
				fout.write(' {0}'.format(tile))
		fout.write('\n')
	fin.close()
	fout.flush()
	fout.close()
