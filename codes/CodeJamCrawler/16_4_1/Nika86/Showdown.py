#! /usr/bin/python

nums = [[1,0,0]]

for i in range(15):
	newNums = nums[-1][:]

	for j in range(3):
		newNums[j] += nums[-1][(j + 2) % 3]

	nums += [newNums]

def nextC(c):
	if c == 'P':
		return 'R'
	elif c == 'R':
		return 'S'
	else:
		return 'P'

def getMinString(n, c):
	if n == 0:
		return c

	s1 = getMinString(n - 1, c)
	s2 = getMinString(n - 1, nextC(c))

	if (s1 < s2):
		return s1 + s2
	else:
		return s2 + s1


T = int(raw_input())

for t in range(1, T+1):
	n, r, p, s = [int(inp) for inp in raw_input().split()]

	if set([p,r,s]) != set(nums[n]):
		print 'Case #' + str(t) + ': ' + 'IMPOSSIBLE'
	else:
		if [p, r, s] == nums[n]:
			c = 'P'
		elif [r, s, p] == nums[n]:
			c = 'R'
		else:
			c = 'S'

		print 'Case #' + str(t) + ': ' + getMinString(n, c)