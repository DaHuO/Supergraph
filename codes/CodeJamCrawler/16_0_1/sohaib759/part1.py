
from copy import deepcopy

def findLast(number):

	if number == 0:
		return "INSOMNIA"

	seen = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	rightnow = 0

	left = 10

	N = 0

	while 1:
		N = N + 1
		rightnow = rightnow + number
		current = deepcopy(rightnow)

		while current:
			# print current
			digit = current % 10
			current //= 10
			if seen[digit] == 0:
				# print "Appended: " + str(digit)
				seen[digit] = 1
				left = left - 1

		if left == 0:
			return rightnow

	return "INSOMNIA"

t = int(raw_input())

for i in xrange(1, t + 1):
	# n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	number = int(raw_input())
	result = findLast(number)
	print "Case #{}: {}".format(i, result)

