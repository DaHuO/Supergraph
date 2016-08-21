from math import sqrt; from itertools import count, islice
from random import randint

get_inp = 0;get_value = []
while True:
	try:
		r = raw_input().strip();
		if get_inp == 0: get_inp = 1; continue
		value = r.split(' '); print "Case #1:"
	except EOFError: break
number_of_digits, total_jamcoins = int(value[0]), int(value[1]); number_of_digits = number_of_digits-2
'''
def mrange(start, stop, step):
	while start < stop:
		yield start
		start += step
def is_prime(num):
    return not any(num % i == 0 for i in mrange(3, int(sqrt(num)) + 1, 2))
'''
def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1

'''def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
'''
def divisorGenerator(n):
    large_divisors = []
    d = 2
    while n > 1:
        if n % d == 0:
            yield d
            n /= d
        else:
            d += 1

randBinList = lambda n: [str(randint(0,1)) for b in range(1,n+1)]
idx = 0
while idx < total_jamcoins:
	a = randBinList(number_of_digits);binary = '1'+"".join(a)+"1"
	prime_numbers = [];jamcoin = []
	for i in range(2,11):
		base_num = int(binary, i)
		if not is_prime(base_num): prime_numbers.append(base_num)
		else: break
	if len(prime_numbers)==9:
		for number in prime_numbers:
			non_trivial_divisor = divisorGenerator(number);
			check_1 = non_trivial_divisor.next()
			if check_1 is not 1:
				jamcoin.append(str(check_1))
			else:
				jamcoin.append(str(non_trivial_divisor.next()))
		jam_string = ' '.join(jamcoin)
		idx+=1
		print "{} {}".format(binary, jam_string)

