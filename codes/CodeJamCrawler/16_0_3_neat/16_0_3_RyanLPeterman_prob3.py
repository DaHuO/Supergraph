import sys

def main():
	with open(sys.argv[1]) as file_handler:
		test_cases = file_handler.read().splitlines()

		# for each test case
		for j in range(1, int(test_cases[0])+ 1):

			# stores case in list of ints
			case = [int(i) for i in test_cases[j].split()]

			N = case[0] # length
			J = case[1] # num jam coins

			# start at 1...00 because we increment when creating valid jamcoin
			last_jamcoin = "1" + "0" * (N - 1)
			ans = []

			sys.stdout.write("Case #" + str(j) + ": \n")
			max_jamcoin = "1" * N

			# for every jam coin to create
			for i in xrange(J):

				ans = create_valid_jamcoin(last_jamcoin, max_jamcoin)
				last_jamcoin = ans[0]

				# sys.stdout.write( answer out
				for item in ans:
					sys.stdout.write(str(item) + " ")

				sys.stdout.write("\n")

# returns [jamcoin, divisor 2, .., divisor 10]
# takes as input the last jamcoin generated so that
# we continue from that one in search of a jamcoin
def create_valid_jamcoin(last_jamcoin, max_jamcoin):


	# increment jamcoin by one from last jamcoin
	curr_jamcoin = increment_jamcoin(last_jamcoin)

	# print "creating jamcoin: " + curr_jamcoin

	# while there are more jamcoins to test
	while curr_jamcoin != max_jamcoin:

		ans = []
		ans.append(curr_jamcoin)
		valid = True

		for radix in xrange(2, 11):

			curr_value = int(curr_jamcoin, radix)
			divisor = find_divisor(curr_value)

			# print "Found Divisor = " +str(divisor) + " for radix = " + str(radix)
			# append divisor for answer if found one
			if divisor:
				ans.append(divisor)
			# not valid jamcoin since prime in one radix
			else:
				valid = False
				break

		# increment string that is jamcoin and convert back to binary string
		curr_jamcoin = increment_jamcoin(curr_jamcoin)

		# print "creating jamcoin: " + curr_jamcoin

		# full answer
		if valid:
			return ans

# returns divisor or false if
def find_divisor(n):

	# easier to try another jamcoin
	check_up_to = 100
	for i in range(3, check_up_to):
	    if n % i == 0:
	        return i
	return False

def test():
	curr_jamcoin = "100001"

	for i in range(3):
		curr_jamcoin = increment_jamcoin(curr_jamcoin)

		for radix in xrange(2, 11):

				curr_value = int(curr_jamcoin, radix)
				sys.stdout.write(str(curr_value) + "   ")

		print "\n"

def increment_jamcoin(last_coin_mid):

	return  '{0:0b}'.format(int(last_coin_mid[:-1], 2) + 1) + "1"

if __name__ == '__main__':
	main()