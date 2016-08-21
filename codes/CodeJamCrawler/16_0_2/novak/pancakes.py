import sys

def flip(n, times):
	if times % 2 == 0:
		return n
	return 1 - n

def to_list(s):
	l = []
	for c in s:
		if c == '-':
			l.append(0)
		else:
			l.append(1)
	return l

def pancakes(stack):
	flips = 0

	for fixed in xrange(len(stack) - 1, -1, -1):
		if not flip(stack[fixed], flips):
			flips += 1

	return flips


def main():
	num_of_cases = int(raw_input())
	for i in xrange(num_of_cases):
		stack = to_list(raw_input())
		print 'Case #%s: %s' % (i + 1, pancakes(stack))

if __name__ == '__main__':
	main()