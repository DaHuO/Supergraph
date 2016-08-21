# fractiles.py
def test(k, c, s):

	if s < k: return 'IMPOSSIBLE'
	if k == 1: return '1'

	x = ''	
	start = 1
	if c > 1: start = 2

	for tile in xrange(start, k+1):

		x = x + str(tile) + ' '
	
	return x

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 	k, c, s = [int(j) for j in raw_input().split(' ')]
 	print "Case #{}: {}".format(i, test(k, c, s))
