def tostr(i, n):
	s = bin(i)[2:]
	return '0'*(n-len(s))+s


def solve(n, total):
	cnt = 0
	res = ''
	for i in range(2**(n-2)):
		if cnt >= total:
			break

		cr = ''
		s = '1'+tostr(i, n-2)+'1'

		cr += s

		ok = True
		for base in range(2, 11):
			g = int(s, base)
			j = 2
			while j*j<=g:
				if g % j == 0:
					cr += ' '+str(j)
					break
				j += 1
			if j*j>g:
				ok = False
				break

		if ok:
			res += cr+'\n'
			cnt += 1

	return res

with open("output.txt", "w") as f:
    res = solve(16, 50)
    print('Case #{}:\n{}'.format(1, res), file=f)
