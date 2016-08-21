#!/usr/bin/env python

import math

def is_prime(n):
    if n == 2:
        return True, 0

    if n % 2 == 0:
    	return False, 2

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False, divisor

    return True, 0

def get_value_in_base(binary, b):

	value = 0
	for i, d in enumerate(binary):
		value += int(d) * int(math.pow(b, len(binary) - i - 1))
	return value

def comp(list1, list2):
    for i, val in enumerate(list1):
        if val != list2[i]:
            return False
    return True

def main():

	filename = "small.txt"
	f = open(filename, 'r')
	o = open(filename + "_out", 'w')

	T = int(f.readline())

	for t in range(T):
		NJ = f.readline().split("\n")[0]
		N = int(NJ.split(' ')[0])
		J = int(NJ.split(' ')[1])

		o.write("Case #" + str(t + 1) + ":\n")

		start = int(math.pow(2, N-1) + 1)
		end = int(math.pow(2, N) - 1)

		j = 0
		while start <= end:
			binary = list("{0:b}".format(start))
			was_prime = False
			divisor_list = []
			for b in range(2, 11):
				isp, divisor = is_prime(get_value_in_base(binary, b))
				divisor_list.append(divisor) 
				if isp:
					was_prime = True
					break
			if not was_prime:
				j += 1
				o.write(''.join(binary))
				for d in divisor_list:
					o.write(" " + str(d))
				o.write("\n")
				if j == J:
					break
			start += 2


if __name__ == "__main__":
	main()
