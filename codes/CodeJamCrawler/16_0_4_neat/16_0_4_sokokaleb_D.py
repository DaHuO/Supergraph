import sys

def CASE(tcno):
	sys.stdout.write('Case #' + str(tcno) + ':')

def dfs(d, pos, suda, pkt, k):
	# sys.stderr.write('(' + str(pos) + ', ' + str(d) + ')\n')
	if d == 0:
		sys.stdout.write(' ' + str(pos + 1))
		return
	if suda < k:
		dfs(d - 1, pos + pkt * suda, suda + 1, pkt / k, k)
	else:
		dfs(d - 1, pos, suda + 1, pkt / k, k)

def main():
	n = int(raw_input())
	for tc in xrange(n):
		k, c, s = map(int, raw_input().split(' '))
		CASE(tc + 1)
		if s < ((k + c - 1) // c): sys.stdout.write(' IMPOSSIBLE\n')
		else:
			for i in xrange((k + c - 1) // c):
				dfs(c, 0, c * i, k ** (c - 1), k)
			sys.stdout.write('\n')

if __name__ == '__main__':
	main()
