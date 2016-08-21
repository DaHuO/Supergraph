import itertools
import math
def isPrime(num):
	for i in range(2, int(math.sqrt(num))):
	    if (num % i) == 0:
	        return i

	return 0


def get_valid_nums(N, J):
	output_file = open('out.txt', 'w')
	output_file.write("Case #1:\n")
	all_combs = list(itertools.product(['0', '1'], repeat=N-2))
	count = 0

	for test_num in all_combs:
		test_num = list(test_num)
		test_num.insert(0, '1')
		test_num.append('1')
		notPrime = True
		divisors = []

		for base in range(2, 11):
			check_num = int(''.join(test_num), base)
			div = isPrime(check_num)
			if(div == 0):
				notPrime = False
				break
			else:
				divisors.append(div)

		if(notPrime):
			count += 1
			print count
			output_file.write("".join(test_num) + " " + " ".join([str(i) for i in divisors]) + "\n")
			if(count == J):
				break


input_file = open('C-small-attempt0.in', 'r').readlines()
n = int(input_file[1].split(" ")[0].strip())
j = int(input_file[1].split(" ")[1].strip())
get_valid_nums(16, 50)

