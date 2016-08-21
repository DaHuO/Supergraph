import math

def generate_possible_jam_coin (n, i):
	return "1" + format(i, '0' + str(n-2) + 'b') + "1"

def get_non_trivial_divisor(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return i
	return -1


t = int(raw_input()) 
for i in xrange(1, t + 1):
   n, j = [int(s) for s in raw_input().split(" ")] 
   print "Case #{}:".format(i)
   number_jam_coins = 0
   for k in range(0, int(math.pow(n-2, 2))):
   	possible_jam_coin = generate_possible_jam_coin(n, k)
   	is_jam_coin = True
   	l_divisors = []
   	for base in range(2,11):
   		base_number =  int(possible_jam_coin, base)
   		divisor = get_non_trivial_divisor(base_number)
   		if (divisor == -1):
   			is_jam_coin = False
   			break
   		else:
   			# l_divisors.append(base_number)
   			l_divisors.append(divisor)
   	if (is_jam_coin):
   		print possible_jam_coin, " ".join(map(str, l_divisors))
   		number_jam_coins += 1
   		if (number_jam_coins == j):
   			break




