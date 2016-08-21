import random
import math
T = 0
N = 0
J = 0
counter = 0
jamcoins = []
success_list = []

def change_base(num, base):
	changed_num = 0
	i = 0
	while num != 0:
		changed_num += (num % 10) * math.pow(base, i)
		i += 1
		num /= 10
	return int(changed_num)

def prime(num):
	for i in range(2, int(math.ceil(math.sqrt(num)) + 1)):
		if num % i == 0:
			return False, i
	return True, 0

def jamcoin(value, length):
	non_trivial_factor = []
	if value % 10 != 1 and value / (10 * length) != 1:
		return False, []
	for i in range(2, 11):
		base = change_base(value, i)
		is_prime, factor = prime(base)
		if is_prime:
			return False, []
		non_trivial_factor.append(factor)
	return True, non_trivial_factor

def create_jamcoins(case_num, N, J):
	global counter, success_list, jamcoins
	if counter == J:
		return
	else:
		value = int(math.pow(10, N-1))
		for i in range(1, N-1):
			value += int(math.pow(random.choice([0, 10]), i))
		value += 1
		is_jamcoin, non_trivial_factor   = jamcoin(value, N)
		if is_jamcoin and value not in success_list:
			success_list.append(value)
			jamcoins.append([value, non_trivial_factor])
			counter += 1
			create_jamcoins(case_num, N, J)
		else:
			create_jamcoins(case_num, N, J)

T = input()
for case_num in range(T):
	N, J = [int(s) for s in raw_input().split(" ")]
	counter = 0
	success_list = []
	jamcoins = []
	create_jamcoins(case_num, N, J)
	print 'Case #%d:' % (case_num + 1)
	for i in jamcoins:
		print i[0], ' '.join(map(str, i[1]))

