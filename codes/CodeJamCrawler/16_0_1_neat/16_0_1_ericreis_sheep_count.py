def sheep_count(n):

	# INSONMIA is return when n = 0
	if n == 0:
		return "INSOMNIA"

	# initializes a vector of marked positions
	v = [0] * 10

	# counter of digits yet to be found
	to_go = 10
	i = 1
	stop = False

	while to_go > 0:
		s = str(n * i)
		for e in s:
			c = int(e)
			if v[c] == 0:
				v[c] = 1
				to_go -= 1
		i += 1

	return n * (i - 1)


def main():
	t = int(input())

	result = []

	for i in xrange(1, t + 1):
		n = int(input())
		
		result.append(sheep_count(n))

	for i in xrange(len(result)):
		print("Case #{}: {}".format(i + 1, result[i]))


main()