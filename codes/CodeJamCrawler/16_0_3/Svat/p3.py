import sys
from math import floor,sqrt

def first_divisor(n):
	for x in range(2,int(floor(sqrt(n)))):
		if n % x == 0:
			return x
	return None

def solve(N, J):
	# ends are 1's
	middle = ['0' for x in range(N-2)]
	middle_num = 0
	found = 0
	for i in range(0, 2**(N-2)):
		# go through all possible binary middle numbers
		s = '1' + format(i, '0'+str(N-2)+'b') + '1'
		divisors = [first_divisor(int(s,b)) for b in range(2,11)]
		if all([x is not None for x in divisors]):
			found += 1
			print(s + ' ' + ' '.join(map(str, divisors))) 
			if found == J:
				return

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline().strip())
    [N, J] = [int(x) for x in f.readline().strip().split(' ')]
    # N = length of each jamcoin
    # J = # of jamcoins to return
    for i in xrange(T):
    	print("Case #1:")
        solve(N, J)