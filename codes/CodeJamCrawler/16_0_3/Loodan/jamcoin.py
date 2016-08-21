import itertools
import math

# Process the inputs into a list
def pre_process(file):

	data = []

	f = open(file, 'r')

	temp = list(f)

	data.append(int(temp[0]))

	s = temp[1].split()

	for n in s:

		data.append(int(n)) 

	return data


# Create a list of possible jam coin with length of N
def create_coin(N):

	coins = ["".join(bit) for bit in itertools.product("01", repeat=N)]

	return coins



# Get number with a base
def num_base(coin, base):

	N = len(coin)

	s = 0

	for i in range(N):

		s = s + (base**(N - i - 1))*int(coin[i])

	return s


# Get the number from base 2 to 10 for a coin
def get_base(coin):

	bases = []

	for i in range(2, 11):

		n = num_base(coin, i)

		bases.append(n)

	return bases


# Check if a number is prime
def is_prime(num):

	N = int(math.sqrt(num))

	for div in range(2, N+1):

		if ((num % div) == 0):

			return div

	return 0



# Check if a coin is a jamcoin
def is_jamcoin(coin):

	# Check if head and tail are 1
	if ((coin[0] != "1") or (coin[-1] != "1")):

		return False

	bases = get_base(coin)

	s = ""

	# Check if the number of each base is a prime
	for num in bases:

		factor = is_prime(num)

		if (factor == 0):

			return False

		s = s + "{} ".format(factor)

	return coin + " " + s


if __name__ == "__main__":

	data = pre_process("./C-small-attempt0.in")

	sol = open("./jamcoin.out", "r+")

	N = int(data[2])

	jamcoin = []

	coins = create_coin(int(data[1]))

	i = 0

	while (len(jamcoin) < N):

		if (i > len(coins)):

			break

		c = is_jamcoin(coins[i])

		if (c):

			jamcoin.append(c)

		i = i + 1


	# Wrie to the solution
	sol.write("Case #1:\n")

	for coin in jamcoin:

		sol.write("{}\n".format(coin))

	sol.close()

