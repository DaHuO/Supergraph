def main():
	t = int(raw_input())
	for i in xrange(1, t+1):
		k, c, s = map(int, raw_input().split())
		result = 'IMPOSSIBLE'
		if s >= k:
			result = ' '.join(map(str, xrange(1, k+1)))
		print 'Case #%d: %s' % (i, result)

if __name__ == '__main__':
	main()
