# coin_jam.py
def test(n, j):

	divisors = ' 3 4 5 6 7 8 9 10 11\n'
	result = '1' * n + divisors

	num_of_zero = 2
	loc_of_zero = 1

	while num_of_zero < n:

		while  loc_of_zero < n - num_of_zero:

			coin = '1' * loc_of_zero + '0' * num_of_zero + '1' * (n - num_of_zero - loc_of_zero)
			result = result + coin + divisors
			loc_of_zero += 1
			
		num_of_zero += 2
		loc_of_zero = 1

	return result

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
 	n, j = [int(s) for s in raw_input().split(' ')]
 	print "Case #{}: \n{}".format(i, test(n, j))
