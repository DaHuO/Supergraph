#!coding=utf-8
import sys

def main():
	t = int(raw_input())
	for i in range(1, t+1):
		chars = []
		for c in raw_input():
			chars.append(c)
		print 'Case #%d:' % i, solve(chars)
		continue
	return

def solve(chars):
	if len(chars) == 0:
		return 0
	if chars[-1] == '+':
		return solve(chars[:-1])
	else:
		return minus_solve(chars[:-1]) + 1

def minus_solve(chars):
	if len(chars) == 0:
		return 0
	if chars[-1] == '-':
		return minus_solve(chars[:-1])
	else:
		return solve(chars[:-1]) + 1

if __name__ == '__main__':
	main()