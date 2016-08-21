#!/usr/bin/python2

f = open('C-large.in', 'r')
T = int(f.readline().rstrip()) # Number of test cases.
N, J = map(int, f.readline().split())
f.close()

def jamcoin_check(num):
	potential_jamcoin = bin(num)[2:]
	output_line = potential_jamcoin[:]
	for base in range(2, 11):
		basenum = int(potential_jamcoin, base)
		divisor_found = False
		iter = 2
		if basenum < 1000: itermax = basenum
		else: itermax = 1000 # Pass on any with 1st divisors > 999.
		while iter < itermax:
#		for i in xrange(2, basenum):
			if basenum % iter == 0:
				divisor_found = True
				output_line += " " + str(iter)
				break
			iter += 1
		if divisor_found == False:
			return (False, None)
	return (True, output_line)		


# Starting Point.  Equals lowest possible jamcoin in base2.
base2_iter = int(("1" + (N-2)*"0" + "1"), 2)

print "Case #1:"

result_count = 0
while result_count < J:
	is_jamcoin = jamcoin_check(base2_iter)
	if is_jamcoin[0]:
		print is_jamcoin[1].rstrip()
		result_count += 1
	base2_iter += 2 # jamcoins are odd in base 2, so iter + 2.
