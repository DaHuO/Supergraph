import sys
from itertools import count


cache = {}


def calc():
	x = input()
	if x == 0:
		return 'INSOMNIA'
	elif x in cache:
		return cache[x]
	else:
		pass
	rest = set(map(str, range(10)))
	xx = 0
	i = 0
	while rest:
		xx += x
		i += 1
		rest -= set(str(xx))
	ans = str(xx)
	cache[x] = ans
	return ans


def main():
	T = input()
	for t in range(T):
		ans = calc()
		print 'Case #%d: %s'%(t+1, ans)


if __name__ == '__main__':
	main()
