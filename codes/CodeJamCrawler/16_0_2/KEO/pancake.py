
def regions(stack):
	answer = 0
	length = len(stack)

	if length == 0: return 0

	i, j = 0, 0
	while i < length:
		left = stack[i]

		i += 1
		while j < length and stack[j] == left:
			j += 1
		answer += 1
		i = j

	return answer

T = int(raw_input())

for i in xrange(1, T+1):
	print 'Case #{}:'.format(i),

	state = 0
	stack = raw_input().strip()
	stack = stack.rstrip('+')

	print regions(stack)
