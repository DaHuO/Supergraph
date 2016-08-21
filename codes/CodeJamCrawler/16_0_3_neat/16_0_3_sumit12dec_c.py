N = input()

N, J = map(int, raw_input().split(' '))

results = {}


import itertools
from math import sqrt; from itertools import count, islice

save_for_later = {}

def isPrime(n):
	temp = [n%i for i in islice(count(2), int(sqrt(n)-1))]
	#print temp
	_all = all(temp)
	if not _all:
		save_for_later[n] = temp.index(0) + 2
	return n>1 and _all


def list_of_all_bases(binary_number):
	value_of_all_bases = []
	for i in range(2,11):
		value_of_all_bases.append(int(binary_number, i))
	return value_of_all_bases

def has_prime(pass_me_list):
	for each in pass_me_list:
		if isPrime(each)==True:
			return True
	return False

def get_LCD_of_all_bases(all_bases):
	list_to_return = []
	for each in all_bases:
		list_to_return.append(save_for_later[each])
	return list_to_return



def get_output():
	list_of_probables = ["".join(seq) for seq in itertools.product("01", repeat=N)]
	final_probables = filter(lambda x:x[0]=='1' and x[-1]=='1', list_of_probables)
	final_probables.append('1'*N)

	for each_binary in final_probables:
		all_bases = list_of_all_bases(each_binary)
		if not has_prime(all_bases):
			results[each_binary] = get_LCD_of_all_bases(all_bases)
		if len(results)==J:
			break

	#print results

get_output()

print "Case #1:"
for each in results:
	print "{0} {1}".format(each, " ".join(map(str, results[each])) ) 



