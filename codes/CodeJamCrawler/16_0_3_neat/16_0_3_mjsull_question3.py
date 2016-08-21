import sys
out_file = open(sys.argv[2], 'w')


from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

def rwh_primes2(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


with open(sys.argv[1]) as in_file:
    num_cases = int(in_file.readline().rstrip())
    for i in range(1, num_cases + 1):
        coin_length, num_coins = in_file.readline().split()
        num_coins = int(num_coins)
        coin_length = int(coin_length)
        out_file.write('Case #' + str(i) + ':\n')
        coins = []
        denoms = []
        coin_int = int(str(10 ** (coin_length - 1) + 1), 2)
        last_coin_int = int('1' * coin_length)
        prime_list = rwh_primes2(1000)
        while len(coins) < num_coins:
            coin = "{0:b}".format(coin_int)
            if coin == str(last_coin_int):
                break
            if coin[-1] == '0':
                coin_int += 1
                continue
            the_denomins = []
            for j in range(2, 11):
                the_int = int(coin, j)
                for k in prime_list:
                    if the_int % k == 0:
                        the_denomins.append(k)
                        break
            if len(the_denomins) == 9:
                coins.append(coin)
                denoms.append(the_denomins)
            coin_int += 1
        coin_int = int(str(10 ** (coin_length - 1) + 1), 2)
        while len(coins) < num_coins:
            coin = "{0:b}".format(coin_int)
            if coin[-1] == '0' or coin in coins:
                coin_int += 1
                continue
            the_denomins = []
            for j in range(2, 11):
                the_int = int(coin, j)
                if is_prime(the_int):
                    break
                else:
                    lowest_denom = None
                    x = 2
                    while lowest_denom is None:
                        if the_int % x == 0:
                            lowest_denom = x
                        x += 1
                    the_denomins.append(lowest_denom)
            if len(the_denomins) == 9:
                coins.append(coin)
                denoms.append(the_denomins)
            coin_int += 1
        for j, k in zip(coins, denoms):
            out_file.write(j + ' ' + ' '.join(map(str, k)) + '\n')

