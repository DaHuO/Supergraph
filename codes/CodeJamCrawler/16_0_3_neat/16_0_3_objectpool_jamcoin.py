from itertools import product
from my_math import next_prime

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

def bin_to_base(bit_list, n_base):
	result = 0
	for index, b in enumerate(reversed(bit_list)):
		if b == 1:
			result += n_base**index
	return result

def lowest_non_trivial_divisor(n):
	prime = 2
	while prime < n:
		if n % prime == 0:
			return prime
		prime = next_prime(prime)

	for x in range(2, n):
		if n % x == 0:
			return x
	return None

def get_base_divisor_strs(coin):
	## returns none if coin isn't a jamcoin!
	base_vals = []
	for base in range(2, 11):
		base_vals.append(bin_to_base(coin, base))
		if is_prime(base_vals[-1]):
			# print '+'+str(base), int(coin, base)
			return None
	divs = []
	for y in base_vals:
		divs.append(str(lowest_non_trivial_divisor(y)))
	return divs

num_test_cases = int(input())

for test_case in range(num_test_cases):
	n, j = [int(token) for token in input().split()]
	num_bits = n-2
	print("Case #{0}:".format(test_case+1), end='')
	coin_limit = j
	coin_count = 0
	for inner_jam_number in range(0, 2**num_bits):
		jamcoin_binary_lst = [1] + [(int(inner_jam_number) >> bit) & 1 for bit in range(num_bits - 1, -1, -1)] + [1]
		base_divisor_strs = get_base_divisor_strs(jamcoin_binary_lst)
		if base_divisor_strs is not None:
			print("\n{0} {1}".format(*(''.join(str(c) for c in jamcoin_binary_lst), ' '.join(base_divisor_strs))), end='')
			coin_count += 1
			if coin_count >= coin_limit:
				break