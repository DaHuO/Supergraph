with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])
n, j = lines[1].split()
n, j = int(n), int(j)
f = open('out.txt', 'w')
f.write('Case #1:\n')


def find_prime_numbers(min_n, max_n):
    print 'need primes between', min_n, max_n
    primes = []
    for num in xrange(min_n, max_n + 1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            primes.append(num)
    return primes


max_value = sum([2 ** i for i in xrange(n)])
min_value = 2 ** (n - 1) + 1

n_jamcoins = 0
primes = find_prime_numbers(7, 10000)

for v in xrange(min_value, max_value + 1):
    jamcoin = bin(v)[2:]
    if int(jamcoin[-1]) != 1 or int(jamcoin[0]) != 1:
        continue
    jamcoin_10 = int(jamcoin)
    print '============', jamcoin

    # convert from different systems to base 10
    divisors = [0] * 9
    for dd, base in enumerate(xrange(2, 11)):
        jamcoin_base = 0
        for pow, b in enumerate(jamcoin[::-1]):
            if int(b) == 1:
                jamcoin_base += base ** pow

        # find divisor
        posssible_divisors = [2, 3, 5]
        for p in posssible_divisors:
            if jamcoin_base % p == 0 and jamcoin_base != p:
                divisors[dd] = p
                print 'base', base, 'jamcoin', jamcoin_base, 'divisor', p
                break
        if divisors[dd] == 0:
            for p in primes:
                if jamcoin_base % p == 0 and jamcoin_base != p:
                    divisors[dd] = p
                    print 'base', base, 'jamcoin', jamcoin_base, 'divisor', p
                    break
        if divisors[dd] == 0:
            print 'NOT A JAMCOIN'
            break

    if all(divisors) > 0:
        ans = str(jamcoin)
        for d in divisors:
            ans += ' ' + str(d)
        print ans
        f.write(ans + '\n')
        n_jamcoins += 1
    if n_jamcoins == j:
        break

f.close()
