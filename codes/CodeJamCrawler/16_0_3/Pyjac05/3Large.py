from math import sqrt

def isprime2(x):
    prime = False
    if x > 1:
        prime = True
        k = 2
        n = sqrt(x) # to find square of x only once (or n = x ** 0.5 to get rid of math module)
        while k <= n and prime == True:
            if x % k == 0:
                return False
            k += 1
    return True


def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
def print_factors(x):
	i = 2
	while (i <= x + 1):
		if x % i == 0:
			if isprime(i):
				return i
		if i == 500:
			return 0
		i = i + 1
	
l = input()
for z in range(0, l):
	N, J = map(int,raw_input().split(" "))
	Upper = int("1" + "1" * (N - 2) + "1", 2)
	Lower = int("1" + "0" * (N - 2) + "1", 2)
	i = 1
	print "Case #{0}:".format(z + 1)
	while Lower <= Upper and i <= J:
		lower = bin(Lower)[2:]
		
		if lower[-1] != '1' or lower[0] != '1' or isprime(int(Lower)):
			Lower = Lower + 1
			continue
		S = 's'
		po = []
		for v in range(2, 11):
			a = print_factors(int(lower, v))
			if a == 0:
				S = 'f'
				break
			po.append(str(a))
		if S == 'f':
			Lower = Lower + 1
			continue
		
		print lower, " ".join(po)
		Lower = Lower + 1
		i = i + 1