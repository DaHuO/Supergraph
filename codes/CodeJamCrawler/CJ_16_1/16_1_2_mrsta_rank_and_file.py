# rank_and_file.py
def test(s):

	result = ''

	array  = []

	x = []

	for i in xrange(2501):
		array.append(0)

	for i in xrange(len(s)):
		height = s[i]
		array[height] += 1

	for i in xrange(len(array) - 1):
		if array[i] % 2 != 0: 
			x.append(i)

	for i in xrange(len(x)):
		result = result + str(x[i]) + ' '

	return result

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	j = int(raw_input()) * 2 - 1
	n = []
	for j in xrange(1, j+1):
		for s in raw_input().split(' '):
			n.append(int(s))
 	print "Case #{}: {}".format(i, test(n))