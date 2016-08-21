import sys


def calc():
	pat = raw_input()
	ans = 0
	prev = pat[0]
	for c in pat[1:]:
		if c != prev:
			ans += 1
		prev = c
	if pat[-1] == '-':
		ans += 1
	return str(ans)


def main():
	T = input()
	for t in range(T):
		ans = calc()
		print 'Case #%d: %s'%(t+1, ans)


if __name__ == '__main__':
	main()
