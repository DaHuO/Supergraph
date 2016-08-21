# WORST CODE EVER

import random
import math

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  

def can_be_prime(jamcoin, jamcoin_len):
	jamcoin_string = str(jamcoin)
	for base in range(2, 11):
		value = 0
		for i in range(jamcoin_len, 0, -1):
			if jamcoin_string[i - 1] == "0":
				pass
			else:
				value += base ** (jamcoin_len - i)
		if is_prime(value): return True
	return False

def generate_jamcoin(jamcoin_len):
	jamcoin = ""
	for digit in range(jamcoin_len):
		if digit == 0 or digit == jamcoin_len - 1:
			jamcoin += "1"
		else:
			jamcoin += str(random.randint(0,1))
	return str(jamcoin)

def find_factor(jamcoin, jamcoin_len):
	value = 0
	for i in range(jamcoin_len, 0, -1):
		if jamcoin[i - 1] == "0":
			pass
		else:
			value += base ** (jamcoin_len - i)
	highest = math.ceil(math.sqrt(value))
	for factor in range(2, highest):
		if value % factor == 0:
			return factor

#	while True:
#		factor = random.randint(2, highest)
#		if factor in used_factors: continue
#		if value % factor == 0:
#			return factor
#		else:
#			used_factors.add(factor)

# MAIN STUFF

t = int(input())
jamcoin_len, n_jamcoins = [int(s) for s in input().split(" ")]

jamcoins = set()
useless_jamcoins = set()
n_coins = 0

while n_coins < n_jamcoins:
	jamcoin = generate_jamcoin(jamcoin_len)
	while jamcoin in jamcoins or jamcoin in useless_jamcoins:
		jamcoin = generate_jamcoin(jamcoin_len)
	if can_be_prime(jamcoin, jamcoin_len):
		useless_jamcoins.add(jamcoin)
		continue
	jamcoins.add(jamcoin)
	n_coins += 1

print ("Case #1:")

for jamcoin in jamcoins:
	line = ""
	line += jamcoin
	factors = set()
	for base in range(2, 11):
		line += " "
		line += str(find_factor(jamcoin, jamcoin_len))
	print (line)



