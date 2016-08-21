import itertools

def calculate_sums(m):
	return [sum(row[i] for row in m) for i in range(len(m[0]))]

def solve(case_number):

	print "Case #{}:".format(case_number)
	length, number = [int(s) for s in raw_input().split(" ")]
	max_number = (10 ** length - 1) / 8
	factor = {}

	def get_factor(num):
		for x in range(2, int(num ** 0.5) + 1):
			if num % x == 0:
				return x
		return 1
	powers = {j: [i ** j for i in range(2, 11)] for j in range(length)}
	# smallest numbers for each base
	base = calculate_sums([powers[0], powers[length-1]])

	# generate the binary bits excluding the first and last
	sequences = ["".join(seq) for seq in itertools.product("01", repeat=length-2)]
	count = 0
	for seq in sequences:
		include_power = [powers[length-2-i] for i in range(length-2) if seq[i] == '1']
		include_power.append(base)
		all_numbers = calculate_sums(include_power)
		divisors = [get_factor(i) for i in all_numbers]
		if 1 not in divisors: # all numbers are not prime
			string_rep = '1' + seq + '1'
			print string_rep, ' '.join(map(str,divisors))
			count += 1
			if count == number:
				return

t = int(raw_input())  # read a line with a single integer
for case in xrange(1, t + 1):
	solve(case)

'''
python solution.py <small.in> small.out
python solution.py <large.in> large.out
'''