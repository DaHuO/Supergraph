def smallest_factor(n): # assumes not prime
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return str(i)

def isprime(n):
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

for tc in range(input()):
	print "Case #1:"
	counter = 0
	lng, num = raw_input().split()
	for i in range(2 ** (int(lng) - 1), 2 ** int(lng)):
		coin = str(bin(i))[2:]
		if coin[-1] == '1':
			if isprime(int(coin,2)) == False and isprime(int(coin,3)) == False and isprime(int(coin,4)) == False and isprime(int(coin,5)) == False and isprime(int(coin,6)) == False and isprime(int(coin,7)) == False and isprime(int(coin,8)) == False and isprime(int(coin,9)) == False and isprime(int(coin)) == False:
				print coin + " " + smallest_factor(int(coin,2)) + " " + smallest_factor(int(coin,3)) + " " + smallest_factor(int(coin,4)) + " " + smallest_factor(int(coin,5)) + " " + smallest_factor(int(coin,6)) + " " + smallest_factor(int(coin,7)) + " " + smallest_factor(int(coin,8)) + " " + smallest_factor(int(coin,9)) + " " + smallest_factor(int(coin,10))
				counter = counter + 1
				if counter == int(num):
					break