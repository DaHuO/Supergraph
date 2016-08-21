import numpy as np
# NumPy source can be installed with "git clone git://github.com/numpy/numpy.git numpy"
import itertools
from math import ceil


# this function not used for small version. might have to write segmented sieve for large input
def primes_sieve(n):
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    for i in xrange(1, int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[k*k/3::2*k]=False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]


def base_k_to_dec(n, k):
    """Return conversion of int n from base k to base 10"""
    dec = 0
    for idx, val in enumerate(n):
        dec += int(val) * k ** (len(n)-idx-1)
    return dec


def is_prime(n):
    """Return (True,0) if int n is prime and (False, i) if not prime where i is a factor"""
    for i in range(2, int(ceil(n**0.5))):
        if n%i==0:
            return False, i
    return True, 0


def is_prime_any_base(n):
    """Check if binary string n is prime in base 2-9"""
    factors = []
    for i in range(2, 11):
        # convert n is base k and convert to decimal
        temp_int = base_k_to_dec(n, i)
        # check if prime
        (is_prime_flag, low_factor) = is_prime(temp_int)
        if is_prime_flag:
            return True, []
        else:
            factors.append(low_factor)
    return False, factors


def generate_potential_jamcoin(n):
    """Generate all strings of 0 and 1 that begin and end as 1"""
    pre_list = map(list, itertools.product([0, 1], repeat=n-2))
    string_list = []
    for idx, entry in enumerate(pre_list):
        pre_list[idx] = [1] + entry + [1]
        stringified = ''.join(str(x) for x in pre_list[idx])
        string_list.append(stringified)
    return string_list


def openfile(input_file):
    """
    Open a file location given as a function parameter and return a list of strings containing lines in the file.
    :param input_file: file location of file to be opened
    :return: my_list: list of strings containing lines in the file
    """
    with open(input_file) as f:
        my_list = f.read().splitlines()
    return my_list

# N = 16, J = 50
if __name__ == '__main__':
    # read input
    input_list = openfile('C-small-attempt0.txt')
    # open output file
    f = open('C-small-solution0.txt', 'w')
    num_cases = int(input_list[0])
    # iterate through cases
    for i in range(1, num_cases + 1):
        params = input_list[i].split()
        N = int(params[0])
        J = int(params[1])
        f.write("Case #{}:\n".format(i))

        found_count = 0
        potential_jamcoins = generate_potential_jamcoin(N)
        for jamcoin in potential_jamcoins:
            (prime_flag, factor) = is_prime_any_base(jamcoin)
            if not prime_flag:
                found_count += 1
                f.write("{} {} {} {} {} {} {} {} {} {}\n".format(jamcoin, factor[0], factor[1], factor[2], factor[3],
                                                              factor[4], factor[5], factor[6], factor[7], factor[8]))
                if found_count >= J:
                    break
    f.close()