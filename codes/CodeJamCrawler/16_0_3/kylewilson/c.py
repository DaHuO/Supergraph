import sys
import math

# Purpose: generate 50 jamcoins of length 16

def divisor(x):
	# returns a divisor of the current number
	# if prime, it returns -1
	lim = int(math.sqrt(x))
	for f in range(2, lim):
		if x % f == 0:
			return f
	return -1

def answer():
	coins = []
	dec_value = 32769
	while dec_value < 65534 and len(coins) < 50:
		bin_string = "{0:b}".format(dec_value)
		coin = [bin_string]
		dec_value += 2
		for base in range(2,11):
			curr_num = int(bin_string, base)
			d = divisor(curr_num)
			if d == -1:
				break
			else:
				coin.append("{}".format(d))
		if len(coin) == 10:
			coins.append(coin)
	print "Case #1:"
	for coin in coins:
		print ' '.join(coin)

answer()