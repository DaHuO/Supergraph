
def alpha(word):

	ans = word[0]
	length = len(word)

	for i in xrange(1, length):

		if word[i] >= ans[0]:

			ans = word[i] + ans 

		else:

			ans = ans + word[i]

	return ans

tt = int(raw_input())
que = []

for i in xrange(0, tt):

	a = raw_input()
	que.append(a)

ans = []

for i in xrange(0, tt):

	print 'Case #%d: %s' % (i+1, alpha(que[i]))


