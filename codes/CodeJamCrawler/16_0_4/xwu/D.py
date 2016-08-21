import sys


def calc():
	K, C, S = [int(x) for x in raw_input().split()]
	ans = []
	if S == K:
		span = K ** (C-1)
		for i in range(K):
			ans.append(span * i + 1)
	else:
		pass
	if ans:
		return ' '.join(map(str, ans))
	else:
		return 'IMPOSSIBLE'


def main():
	T = input()
	for t in range(T):
		ans = calc()
		print 'Case #%d: %s'%(t+1, ans)


if __name__ == '__main__':
	main()
