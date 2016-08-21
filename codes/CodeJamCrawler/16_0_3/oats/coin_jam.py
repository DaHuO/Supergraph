#
#	Arshan Alam
#
#	Google Code Jam 2016
#
#	Coin Jam
#
import math

bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
found_coins = list()

def num_from_base(base, bits):
	"""
	Get the base 10 value of the given bits to the given base.
	:param base: Positive integer denoting the working base.
	:param bits: List of 0-s and 1-s representing the bits of the number.
	:return int: Positive integer.
	"""
	num = 0
	for i, b in enumerate(reversed(bits)):
		if b == 1:
			num += base ** i
	return num

def is_prime(n):
	"""
	Determine if the given integer is prime.
	:param n: Positive integer.
	:return Boolean: True if n is prime, otherwise False.
	"""
	if n == 2:
		return True
	elif (n < 2) or ((n%2) == 0):
		return False
	for i in range(3, int(math.sqrt(n))+1, 2):
		if ((n%i) == 0):
			return False
	return True

def get_nontrivial(coin):
	"""
	Get a list of nontrivial divisor, of the jam coin, for each valid base
	"""
	nontrivial = list()
	for base in bases:
		num = num_from_base(base, coin)
		if (num % 2) == 0:
			nontrivial.append(2)
			continue
		for i in range(3, int(math.sqrt(num))+1, 2):
			if (num % i) == 0:
				nontrivial.append(i)
				break
	return nontrivial

def is_jam(coin):
	"""
	Determine if the given coin is a Jam coin.
	:param coin: list of bits
	:return Boolean: True if coin is Jam, otherwise False.
	"""
	dec_val = num_from_base(2, coin)
	if dec_val in found_coins:
		return False

	for base in bases:
		num = num_from_base(base, coin)
		if is_prime(num):
			return False
	
	found_coins.append(dec_val)
	return True

def dec_to_bin(num):
	"""
	Convert the decimal number into a list of binary bits.
	:param num: Positive integer
	:return list: List of 0s and 1s
	"""
	quotient = int(num) / 2
	remainder = int(num) % 2
	bits = [remainder]
	while quotient != 0:
		remainder = int(quotient) % 2
		quotient = int(quotient) / 2
		bits.insert(0, remainder)
	if (bits[0] == 0):
		bits.pop(0)
	return bits

for test in range(1, int(input())+1):
	coin_info = str(input()).split()
	coin_len = int(coin_info[0])
	num_coins = int(coin_info[1])
	
	coin = [1] + [0]*(coin_len-2) + [1]
	
	min_num = num_from_base(2, coin)
	max_num = num_from_base(2, [1]*coin_len)

	print("Case #" + str(test) + ":")
	
	for num in range(min_num, max_num+1, 2):
		cur_coin = dec_to_bin(num)
		if is_jam(cur_coin):
			num_coins -= 1
			print("".join(map(str, cur_coin)) + " "  + " ".join(map(str, get_nontrivial(cur_coin))))
		if num_coins == 0:
			break
