#
#"{0:b}".format(10)
def isprime(n):
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return True

for num in range(32769,65535):
	if num%2==0:
		continue
	prime = False
	ans = []
	for b in range(2,11):
		x = isprime(int("{0:b}".format(num), b))
		if x == True:
			prime = True
			break
		else:
			ans = ans + [x]
	if not prime:
		print("{0:b}".format(num), end=" ")
		for n in ans:
			print(n, end=" ")
		print()