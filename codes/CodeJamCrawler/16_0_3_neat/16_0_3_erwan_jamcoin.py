import sys
import math

def strings01(string_size):
	result = []
	bin_format = '0' + str(string_size-2) + 'b'
	for i in range(0,1+int(math.pow(2,string_size-2))):
		result.append('1' + format(i, bin_format) + '1')

	return result

def findFirstDivisor(x):
	y = 2
	sroot = math.sqrt(x)
	while y <= sroot:
		if x % y == 0:
			return y
		y += 1
	return 1

case_num = 0
for line in sys.stdin:
	if case_num > 0:
		print 'Case #%d:' % case_num
		NJ = line.rstrip('\n').split(' ')
		N = int(NJ[0])
		J = int(NJ[1])
		jamcoin_count = 0
		for candidate in strings01(N):
			is_jamcoin = True
			divisors = []
			for base in range(2,11):
				base_num = int(candidate,base)
				divisor = findFirstDivisor(base_num)
				if divisor > 1:
					divisors.append(divisor)
				else:
					is_jamcoin = False
					break
			if is_jamcoin:
				print '%s %s' % (candidate, ' '.join(map(str, divisors)))
				jamcoin_count += 1
			if jamcoin_count == J:
				break
		
	case_num += 1
