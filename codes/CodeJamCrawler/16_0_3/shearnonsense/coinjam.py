length = 32
num_unique = 500

jamcoins = []
jamcoin_factors = []

primes = [2]
max_prime = 2

def a_factor(n):
	for p in primes:
		if n % p == 0:
			return p

	# for x in range(max_prime+1, int(n**0.5)+1, 2):
	# 	if n % x == 0:
	# 		return x

	return 0

for i in range(3, 100000, 2):
	if (a_factor(i) == 0):
		primes.append(i)

print(primes)

def jam_str(jamcoin):
	return "{0:b}".format(jamcoin)

def output_for_result(jamcoin, factors):
	return "{} {}\n".format(jam_str(jamcoin), " ".join([str(f) for f in factors]))

# start with 11..11 and subtract 2, 4, 6, ...

max_jamcoin = 2**length - 1
min_jamcoin = 2**(length-1) + 1


for jamcoin in range(min_jamcoin, max_jamcoin, 2):
	factors = []
	is_jamcoin = True
	coin_str = jam_str(jamcoin)

	for base in range(2, 11):
		val_in_base = int(coin_str, base)
		print("Base {}: {}".format(base, val_in_base))
		factor = a_factor(val_in_base)
		if factor != 0:
			factors.append(factor)
		else:
			is_jamcoin = False
			break

	if is_jamcoin:
		jamcoins.append(jamcoin)
		jamcoin_factors.append(factors)

		print("Found jamcoin {}/{}".format(len(jamcoins), num_unique))
		print(output_for_result(jamcoin, factors))

		if len(jamcoins) == num_unique:
			break

with open("coinjam_output.txt", "w") as f:
	f.write("Case #1:\n")
	for i in range(num_unique):
		f.write("{} {}\n".format(jam_str(jamcoins[i]), " ".join([str(f) for f in jamcoin_factors[i]])))