import string
prime_dict = {}

def is_not_prime(x):
    try:
        return prime_dict[x]
    except KeyError:
        num_tries = min(10000000, (x//2)+1)
        for i in range(2, num_tries):
            if x%i == 0:
                prime_dict[x] = i
                break
        else:
            prime_dict[x] = False

    return prime_dict[x]


def precompute(N, J):
    """TODO: Docstring for precompute.

    :N: TODO
    :returns: TODO

    """
    numbers = [[set() for _ in range(33)] for _ in range(11)]
    found = 0


    for i in range(2**(N-1)+1, 2**N, 2):
        binary = "{0:b}".format(i)
        divisors = []

        for base in range(2,11):
            try:
                divisor_or_prime = is_not_prime(int(binary, base))
                if not bool(divisor_or_prime):
                    #print(binary+'not')
                    #print('{} in prime'.format(i))
                    break
                else:
                    divisors.append(str(divisor_or_prime))
            except ValueError as e:
                break
                # print(e)
        else:
            print('{} {}'.format(binary, ' '.join(divisors)))
            found += 1
            if found >= J:
                return


if __name__ == "__main__":
    #N, J = 16,50
    N, J = 32,500
    N, J = 6,3
    numbers = precompute(N, J)

    # primes = precompute_primes(N)
    # numbers = precompute(N, primes)
