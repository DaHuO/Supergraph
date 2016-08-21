import numpy as np

def solve(status):
	l = [None]
	for item in status:
		if item != l[-1]:
			l.append(item)
	l = map(lambda x: 2 if x == '-' else 0, l)[1:-1]
	print l

	ans = sum(l)
	if l[0] == 2:
		ans -= 1

	return ans

if __name__ == '__main__':
	f = open('test.txt')
	o = open('output.txt', 'w')
	for index, line in enumerate(f.readlines()[1:]):
		ans = solve(line)
		o.write("Case #%d: %d\n" % (index + 1, ans ))
