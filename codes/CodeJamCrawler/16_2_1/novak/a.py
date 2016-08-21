import sys

def read_int():
	return int(raw_input())

def read_int_list():
	return [int(x) for x in raw_input().split(' ')]

digits = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

test_cases = read_int()
for test_case in xrange(1, test_cases + 1):
	S = raw_input()

	zero = S.count('Z')
	two = S.count('W')
	four = S.count('U')
	six = S.count('X')
	eight = S.count('G')

	one = S.count('O') - two - zero - four
	seven = S.count('S') - six
	five = S.count('V') - seven
	nine = S.count('I') - five - eight - six
	three = S.count('H') - eight

	answer = zero * '0' + one * '1' + two * '2' + three * '3' + four * '4' + five * '5' + six * '6' + \
	seven * '7' + eight * '8' + nine * '9'

	print 'Case #{}: {}'.format(test_case, answer)