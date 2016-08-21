import math

BIT_STR_LENGTH = 16
NUM_STRS = 50

def generate_bitstrings(length, curr_str, bit_strs):
	if length == 1:
		bit_strs.append(curr_str + "1")
	elif length == BIT_STR_LENGTH:
		generate_bitstrings(length - 1, curr_str + "1", bit_strs)
	else:
		generate_bitstrings(length - 1, curr_str + "0", bit_strs)
		generate_bitstrings(length - 1, curr_str + "1", bit_strs)

def solver(bit_strs):
	valid_strs = []
	for i, bit_str in enumerate(bit_strs):
		if i % 1000 == 0:
			print i
		if bit_str[0] != "1" or bit_str[len(bit_str) - 1] != "1":
			continue
		divisors = []
		for i in range(2, 10 + 1):
			prime_info = primality(int(bit_str, i))
			if prime_info[0]:
				break
			else:
				divisors.append(str(prime_info[1]))
		if len(divisors) == 9:
			valid_strs.append(bit_str + " " + " ".join(divisors))
		if len(valid_strs) == NUM_STRS:
			return valid_strs


def primality(num):
	for i in range(2, int(math.sqrt(num) + 1)):
		if num % i == 0:
			return (False, i)
	return (True,)

if __name__ == "__main__":
	bit_strs = []
	generate_bitstrings(BIT_STR_LENGTH, "", bit_strs)
	valid_strs = solver(bit_strs)
	with open("codejam-c.out", "w") as f:
		f.write("Case #1:\n")
		f.write("\n".join(valid_strs))
		f.close()