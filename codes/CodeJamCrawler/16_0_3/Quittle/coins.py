import itertools
import math
import sys

class Jamcoin:
    __base_two = None
    __divisors = None

    def __init__(self, base_two, divisors):
        assert_is_string(base_two)
        assert len(base_two) > 0
        assert_is_numeric_list(divisors)
        for divisor in divisors:
            assert divisor > 1
            #assert get_smallest_divisor(divisor) is None
        assert len(divisors) == 9, len(divisors)

        self.__base_two = base_two
        self.__divisors = divisors

    def get_base_two(self):
        return self.__base_two

    def get_divisors(self):
        return list(self.__divisors)


def main():
    num_cases = int(sys.stdin.readline())

    line_num = 1
    for line in sys.stdin:
        line = line.strip()

        length_in_base_two, num_of_jamcoins = (int(n) for n in line.split(' '))

        print 'Case #%d:' % line_num

        jamcoins = compute(length_in_base_two, num_of_jamcoins)
        assert jamcoins is not None
        assert len(jamcoins) == num_of_jamcoins
        for jamcoin in jamcoins:
            base_two = jamcoin.get_base_two()
            divisors = jamcoin.get_divisors()
            assert_is_string(base_two)
            assert_is_numeric_list(divisors)
            assert len(divisors) == 9
            print '%s %s' % (base_two, ' '.join(map(str, divisors)))

        line_num += 1

    assert num_cases == line_num - 1


def assert_is_numeric(n):
    assert type(n) in [int, long]


def assert_is_string(s):
    assert isinstance(s, basestring)


def assert_is_numeric_list(arr):
    for n in arr:
        assert_is_numeric(n)


def assert_is_bool_list(arr):
    for b in arr:
        assert type(b) is bool


def test():
    get_some_primes_test()
    get_smallest_divisor_test()
    build_jamcoin_test()
    convert_from_base_ten_test()
    convert_to_base_ten_test()


def compute(length_in_base_two, num_of_jamcoins):
    '''
        Builds a list with of Jamcoins of the given size and amount.  Returns None if not posible
    '''
    min_value = (1 << length_in_base_two - 1) + 1
    max_value = (1 << length_in_base_two) - 1

    primes = get_some_primes(10)
    primes_without_2 = primes[1:]

    jamcoins = []
    for i in xrange(3, len(primes_without_2)):
        for sub_set in itertools.combinations_with_replacement(primes_without_2, i):
            product = reduce(lambda a, b: a * b, sub_set, 1)
            if not (min_value <= product <= max_value):
                continue

            base_two = convert_from_base_ten(product, 2)

            #if base_two[0] != '1' or base_two[-1] != '1':
            #    continue

            divisors = []
            for i in xrange(2, 11):
                new_base = convert_to_base_ten(base_two, i)

                divisor_found = None
                for prime in primes:
                    if new_base % prime == 0:
                        divisor_found = prime
                        break

                if divisor_found is None:
                    break

                divisors.append(prime)

            if len(divisors) == 9:
                jamcoins.append(Jamcoin(base_two, divisors))
                #print 'Jamcoin found: %s. Total Jamcoins: %d' % (base_two, len(jamcoins))
                sys.stdout.flush()
                if len(jamcoins) == num_of_jamcoins:
                    return jamcoins
                continue


    """ This is old work

    jamcoins = []
    # We know we can add two each time since multiples of two don't end in one
    for i in xrange(min_value, max_value, 2):
        jamcoin = build_jamcoin(i)
        print '\r%03d%% (%d)' % ((100 * (i - min_value) / (max_value - min_value)), i),
        sys.stdout.flush()
        if jamcoin is not None:
            print 'Found jamcoin'
            jamcoins.append(jamcoin)
            if len(jamcoins) == num_of_jamcoins:
                return jamcoins
    """
    return None

def get_some_primes(count=100):
    ''' Get some prime numbers '''
    primes = [2]
    i = primes[-1]
    while len(primes) < count:
        divisor_found = False
        for prime in primes:
            if i % prime == 0:
                divisor_found = True
                break

        if not divisor_found:
            primes.append(i)

        i += 1

    return primes


def get_some_primes_test():
    primes = set(get_some_primes())
    assert set([2, 3, 5, 7, 11, 13, 19, 23]).issubset(primes)

    assert 10 == len(get_some_primes(10))
    assert 100 == len(get_some_primes(100))


def quick_prime_check(n):
    ''' Returns 1 if definitely prime, 0 if unknown, or -1 if definitely not prime '''
    if n == 0 or n == 1:
        return 1

    if n in is_prime.known_primes:
        return 1

    if str(n)[-1] in '024568':
        return -1

    for prime in is_prime.known_primes:
        if n % prime == 0:
            return -1

    return 0

def is_prime(n):
    assert_is_numeric(n)

    quick_check = quick_prime_check(n)

    if quick_check == 1:
        return True
    elif quick_check == -1:
        return False


    known_primes = is_prime.known_primes

    highest_prime = known_primes[-1]
    if n > highest_prime:
        sqrt_n = math.sqrt(n)

        for i in itertools.count(highest_prime + 1, 2):
            if i > sqrt_n:
                known_primes.append(i)
                return True

            quick_check = quick_prime_check(i)

            if quick_check == 1:
                assert False, 'We should have already caught this number'
            elif quick_check == -1:
                continue

            assert quick_check == 0

            #print 'Adding prime: ' + str(i)
            #print 'Number of primes: %d while finding primenes of %d' % (len(known_primes), n)
            known_primes.append(i)
            if n % i == 0:
                return False

    return n in known_primes


is_prime.known_primes = [2, 3, 5]

def get_smallest_divisor(n):
    ''' If n is prime, returns None, otherwise returns the smallest divisor of n '''
    assert_is_numeric(n)

    if is_prime(n):
        return None

    for i in is_prime.known_primes:
        if n % i == 0:
            return i

    assert False, 'Not reached'


def get_smallest_divisor_test():
    assert None == get_smallest_divisor(1)
    assert None == get_smallest_divisor(2)
    assert None == get_smallest_divisor(3), get_smallest_divisor(3)
    assert 2    == get_smallest_divisor(4)
    assert None == get_smallest_divisor(5), get_smallest_divisor(5)
    assert 2    == get_smallest_divisor(6)
    assert None == get_smallest_divisor(7)
    assert 2    == get_smallest_divisor(8)
    assert 3    == get_smallest_divisor(9)
    assert 2    == get_smallest_divisor(10)
    assert None == get_smallest_divisor(11)
    assert 2    == get_smallest_divisor(12)
    assert None == get_smallest_divisor(13)
    assert 5    == get_smallest_divisor(55)
    assert 13   == get_smallest_divisor(221)


def build_jamcoin(n):
    ''' Returns the Jamcoin version of n if valid, otherwise returns None '''
    assert_is_numeric(n)

    # Ensure it starts and ends with 1 in Base-2
    base_two = convert_from_base_ten(n, 2)
    if base_two[0] != '1' or base_two[-1] != '1':
        return None

    divisors = []
    # Ensure all Base-N values are non-prime
    for i in xrange(2, 11):
        divisor = get_smallest_divisor(convert_to_base_ten(base_two, i))
        if divisor is None:
            return None
        divisors.append(divisor)

    return Jamcoin(base_two, divisors)


def build_jamcoin_test():
    for i in xrange(3):
        assert None == build_jamcoin(i)
    #assert None != build_jamcoin(35)


def convert_from_base_ten(n, new_base):
    assert_is_numeric(n)
    assert_is_numeric(new_base)
    assert 0 < new_base < 10

    ret = ''
    for i in xrange(0, n):
        ret = str(int(math.floor(n / (new_base ** i)) % new_base)) + ret

    # Lazy method of trimming for now. There is a better way by simply not going all the way up to
    # n, but I'm too tired to think through it
    ret = ret.lstrip('0')

    assert '.' not in ret
    return  '0' if ret == '' else ret


def convert_from_base_ten_test():
    assert '0' == convert_from_base_ten(0, 2), convert_from_base_ten(0, 2)
    assert '0' == convert_from_base_ten(0, 3)
    assert '0' == convert_from_base_ten(0, 6)
    assert '0' == convert_from_base_ten(0, 8)
    assert '0' == convert_from_base_ten(0, 9)

    assert '1' == convert_from_base_ten(1, 2), convert_from_base_ten(1, 2)
    assert '1' == convert_from_base_ten(1, 3), convert_from_base_ten(1, 3)
    assert '1' == convert_from_base_ten(1, 6)
    assert '1' == convert_from_base_ten(1, 8)
    assert '1' == convert_from_base_ten(1, 9)

    assert '10' == convert_from_base_ten(2, 2), convert_from_base_ten(2, 2)
    assert '2' == convert_from_base_ten(2, 3), convert_from_base_ten(2, 3)
    assert '2' == convert_from_base_ten(2, 6)
    assert '2' == convert_from_base_ten(2, 8)
    assert '2' == convert_from_base_ten(2, 9)

    assert '1010' == convert_from_base_ten(10, 2), convert_from_base_ten(10, 2)
    assert '101' == convert_from_base_ten(10, 3)
    assert '14' == convert_from_base_ten(10, 6), convert_from_base_ten(10, 6)
    assert '12' == convert_from_base_ten(10, 8)
    assert '11' == convert_from_base_ten(10, 9)


def convert_to_base_ten(n, from_base):
    assert_is_string(n)
    assert_is_numeric(from_base)
    assert 2 <= from_base < 11

    return int(n, from_base)


def convert_to_base_ten_test():
    assert 0 == convert_to_base_ten('0', 2), convert_to_base_ten('0', 2)
    assert 0 == convert_to_base_ten('0', 3)
    assert 0 == convert_to_base_ten('0', 6)
    assert 0 == convert_to_base_ten('0', 8)
    assert 0 == convert_to_base_ten('0', 9)

    assert 1 == convert_to_base_ten('1', 2), convert_to_base_ten('1', 2)
    assert 1 == convert_to_base_ten('1', 3), convert_to_base_ten('1', 3)
    assert 1 == convert_to_base_ten('1', 6)
    assert 1 == convert_to_base_ten('1', 8)
    assert 1 == convert_to_base_ten('1', 9)

    assert 2 == convert_to_base_ten('10', 2), convert_to_base_ten('10', 2)
    assert 2 == convert_to_base_ten('2', 3), convert_to_base_ten('2', 3)
    assert 2 == convert_to_base_ten('2', 6)
    assert 2 == convert_to_base_ten('2', 8)
    assert 2 == convert_to_base_ten('2', 9)

    assert 10 == convert_to_base_ten('1010', 2), convert_to_base_ten('1010', 2)
    assert 10 == convert_to_base_ten('101', 3)
    assert 10 == convert_to_base_ten('14', 6), convert_to_base_ten('14', 6)
    assert 10 == convert_to_base_ten('12', 8)
    assert 10 == convert_to_base_ten('11', 9)


if __name__ == '__main__':
    test()
    #print 'All tests passed'
    main()