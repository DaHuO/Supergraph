import sys
from itertools import izip
from collections import deque

# f = sys.stdin
f = open('C-small-attempt1.in')
# f = open('test')
o = open('testou3-1.out', 'w')
# o = sys.stdout

def isprime(n):
    n = abs(int(n))

    if n == 2: 
        return True    

    if not n & 1: 
        return False

    for x in xrange(3, int(n**0.5) + 1, 2):
        if n % x == 0:
			# print x, n
			return False

    return True


def ten_to_bin(x):
	return bin(x)[2:]


def ok(x):
	for i in range(2, 11):
		# print ten_to_bin(x), 'is', int(ten_to_bin(x), i), 'in', i
		if isprime(int(ten_to_bin(x), i)):
			# print '\t\tis prime'
			return False
	return True

def dvm(x):
	result = []

	for i in range(2, 11):
		l = int(ten_to_bin(x), i)

		for qq in xrange(2, int(l**0.5) + 1, 1):
			if l % qq == 0:

				result.append(qq)
				break

	return map(str, result)

if __name__ == "__main__":
	total = f.readline()
	
	for i in range(int(total)):
		n, j = map(int, f.readline().strip().split())
		mn = int(''.join(['1'] + ['0'] * (n - 2) + ['1']), 2)
		mx = int(''.join(['1'] + ['1'] * (n - 2) + ['1']), 2)

		o.write('Case #1\n')

		x = mn

		for i in xrange(j):
			while True:
				if ok(x) or x > mx:	
					print x
					o.write(ten_to_bin(x) + ' ' +  ' '.join(dvm(x)) + '\n')
					x += 2
					break
				x += 2
				

		