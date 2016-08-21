input_filename = "C-large.in"
print 'Case #1: ' # ...

# find 500 32 bit numbers that are not prime when interpreted as numbers in bases 2-10

# my solution just tries to divide the number in each base by the first 10 primes,
# and if that doesn't work assume the jam coin is prime and try the next one
# This works because composites are very common

first_ten_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def get_jam_coin_factors(coin):
    factors_for_bases = []
    for base in range(2, 11):
        coin_in_base = int(coin, base)
        try:
            possible_factors = [coin_in_base % prime for prime in first_ten_primes]
            # raises ValueError if there is no 0 in possible_factors
            factor = first_ten_primes[possible_factors.index(0)]
            factors_for_bases.append(factor)
        except ValueError:
            return False # might be prime
    return factors_for_bases


with open(input_filename, 'r') as f:
    f.readline()
    coin_size, number_of_coins_wanted = [int(x) for x in f.readline().split()]
    found_coins = 0
    coin = 2**(coin_size-1)
    while found_coins != number_of_coins_wanted:
        coin += 1
        coin_binary = bin(coin)[2:] # remove the "0x"
        if coin_binary.endswith('0'):
            continue # jamcoins start/end with 1

        factors = get_jam_coin_factors(coin_binary)
        if factors:
            print coin_binary, ' '.join(str(x) for x in factors)
            found_coins += 1





