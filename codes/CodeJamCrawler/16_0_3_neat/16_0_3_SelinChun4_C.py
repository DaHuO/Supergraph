import math

def create_coin_string(n):
    actual_digits = n - 2

    coin_strings = []

    for i in range(int(math.pow(2, actual_digits))):
        s = format(i, '#018b')
        s = s[(-actual_digits):]
        s = '1' + s + '1'

        coin_strings.append(s)
    return coin_strings

def check_jamcoin(coin_string, primes):
    divisor_lst = []
    for i in range(2, 11):
        n = 0
        j = 0
        for digit in reversed(coin_string):
            n += int(math.pow(i, j)) * int(digit)
            j += 1

        if n in primes:
            return []

        else:
            for num in primes:
                if n % num == 0:
                    divisor_lst.append(num)
                    break

    return divisor_lst

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def find_not_primes(n, primes):
    not_primes_lst = []
    for i in range(len(primes) - 1):
        for j in range(primes[i]+1, primes[i+1]):
            not_primes_lst.append(j)

    for j in range(primes[-1], n+1):
        not_primes_lst.append(j)

    return not_primes_lst

primes = rwh_primes(65536)
not_primes = find_not_primes(65536, primes)
t = raw_input()
n, j = map(int, raw_input().split(' '))

print 'Case #1:'
coin_strings = create_coin_string(n)
cnt = 0
for coin_string in coin_strings:
    #divisor_lst = check_jamcoin(coin_string, primes, not_primes)
    divisor_lst = check_jamcoin(coin_string, primes)

    if len(divisor_lst) == 9:
        print coin_string,
        for divisor in divisor_lst[:-1]:
            print divisor,
        print divisor_lst[-1]
        cnt += 1

    if cnt == j:
        break