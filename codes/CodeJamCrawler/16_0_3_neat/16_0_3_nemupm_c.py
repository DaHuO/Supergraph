num_test_cases = input()
len_of_jamcoins, num_of_jamcoins = map(int,raw_input().split())
print "Case #1:"
init_num = 2 ** (len_of_jamcoins-1) + 1

def has_nontrivial_divisor(num):
	for divisor in [2,3,5,7,11,13,17,19]:
		if num % divisor == 0:
			return num / divisor
	return False

for jami in xrange(2 ** (len_of_jamcoins - 2)):
	# 1[1/0][1/0][1/0],,,[1/0][1/0]1
	ans = str(bin(init_num))[2:]
	is_jamcoin = True
	for base in xrange(2,11):
		num_on_base = int(str(bin(init_num))[2:], base)
		result = has_nontrivial_divisor(num_on_base)
		if not result:
			is_jamcoin = False
			break
		else:
			ans += " %d" % result
	if is_jamcoin:
		print ans
		num_of_jamcoins -= 1
		if num_of_jamcoins == 0:
			break
	init_num += 2