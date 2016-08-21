#!coding=utf-8
import sys

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		strs = raw_input().split(' ')
		print 'Case #%d:' % i, solve(strs[0], strs[1], strs[2])
	return

def power(k,c):
	s = 1
	while c > 0:
		s = s * k
		c = c - 1
	return s

def solve(k,c,s):
	k = int(k)
	c = int(c)
	s = int(s)
	invalid = 'IMPOSSIBLE'
	atleast = (k+1) / 2
	if (c == 1 and s < k) or s < atleast:
		return invalid
	solutions = []
	if c == 1:
		for i in range(1, k+1):
			solutions.append(str(i))
		return ' '.join(solutions)
	for i in range(atleast):
		pos = 2*i*power(k,c-1) + 2*i + 1 + 1
		if 2*i+1+1 > k:
			pos = pos -1
		solutions.append(str(pos))
	return ' '.join(solutions)

if __name__ == '__main__':
	main()