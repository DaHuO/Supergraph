import itertools
import math

def binary_to(bin_rep, b):
	num = 0.0
	cp = 0
	while len(bin_rep) > 0:
		cd = int(bin_rep[-1])
		num += cd * b**cp
		cp += 1
		bin_rep = bin_rep[:-1]
	return num


def is_prime(num):
	if num == 1:
		return True, None
	if num == 2:
		return True, None
	if num == 3:
		return True, None

	st = 2
	while st < math.sqrt(num) + 1:
		if (num % st) == 0:
			return False, st
		st += 1
	return True, None

f = open('input.txt')
line = f.readline().split()
num_test_cases = int(line[0])
results = []

for i in xrange(num_test_cases):
	line = f.readline().split()
	N = int(line[0])
	n = N - 2
	J = int(line[1])

	finished = False

	jsf = 0
	while not finished:
		for i in xrange(2**n):
			s = bin(i)[2:]
			s = "0" * (n-len(s)) + s
			s = "1" + s + "1"


			cur_b = s
			all_not_prime = True
			cur_d = []
			for j in xrange(2, 11):
				repres = binary_to(cur_b,j)
				is_p, d = is_prime(repres)
				if is_p:
					all_not_prime = False
					break
				else:
					cur_d.append(d)
			if all_not_prime:
				jsf += 1
				new_str = cur_b
				for cr_d in cur_d:
					new_str = new_str + " " + str(cr_d)

				results.append(new_str)

				if jsf == J:
					finished = True
					break;

f2 = open('output.txt','w')
f2.write("Case #1:\n")
for result in results:
	f2.write(result + "\n")
