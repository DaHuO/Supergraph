import logging, itertools, math

def sieve(n):
    """create a prime sieve up to a given number"""
    is_prime = [False if i % 2 == 0 else True for i in range(0, n)]
    # edge cases
    is_prime[2] = True
    is_prime[1] = False
    for number in range(2, int(math.ceil(math.sqrt(n)))):
        if is_prime[number]:
            for multiple in range(number ** 2, n, number):
                is_prime[multiple] = False
    return is_prime

def pre_calculate_primes(n):
    max_factor = int(math.ceil(math.sqrt(1.2 * (10 ** (n - 1)))))
    logging.info('pre-calculating primes up to %s for n == %s', max_factor, n)
    primes = [idx for idx, prime in enumerate(sieve(max_factor)) if prime]
    logging.info('found %s primes', len(primes))
    return primes

def in_base(base, digits):
    return sum(base ** index for index, digit in enumerate(digits[::-1]) if digit == '1')

def bit_strings_of_length(length):
    return ('1%s1' % each for each in (''.join(bit) for bit in itertools.product('01', repeat = length - 2)))

def find_non_trivial_divisor(primes, x):
    return next((divisor for divisor in primes if x % divisor == 0 and x != divisor), None)

def jamcoins(n, validate):
    return (it for it in (validate(candidate) for candidate in bit_strings_of_length(n)) if it is not None)

def jamcoin_validator(primes):
    def ensure_valid_jamcoin(bit_string):
        logging.info("testing <%s>", bit_string)
        jamcoin = [bit_string]
        for base in list(range(2, 11)):
            value = in_base(base, bit_string)
            logging.info('<%s> == %s in base %s', bit_string, value, base)
            divisor = find_non_trivial_divisor(primes, value)
            if divisor is None:
                logging.info('found no non-trivial divisor for %s', value)
                return None
            logging.info('found %s as divisor', divisor)
            jamcoin.append(divisor)
        return jamcoin
    return ensure_valid_jamcoin

def main(n, j):
    primes = pre_calculate_primes(n)
    validator = jamcoin_validator(primes)
    return itertools.islice(jamcoins(n, validator), j)

def format_coin(coin):
    return ' '.join(str(part) for part in coin)

if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print('Case #1:')
    print('\n'.join(format_coin(each) for each in main(16, 50)))
