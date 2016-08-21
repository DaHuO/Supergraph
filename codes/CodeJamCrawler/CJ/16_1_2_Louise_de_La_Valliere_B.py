from collections import Counter
T = int(raw_input())
for iT in xrange(1, T+1):
	N = int(raw_input())
	counter = Counter()
	for i in xrange(2 * N - 1):
		for x in map(int, raw_input().split()):
			counter[x] += 1
	missing_list = []
	for x in counter:
		if counter[x] % 2:
			missing_list.append(x)
	missing_list.sort()
	print 'Case #%d: %s' % (iT, ' '.join(map(str, missing_list)))