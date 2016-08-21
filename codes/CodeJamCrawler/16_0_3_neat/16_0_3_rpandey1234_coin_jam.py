import sys
import math
import itertools


# Returns a non-trivial divisor of the number if it is not prime, else returns -1
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in xrange(3, int(math.sqrt(n)) + 1, 2):
        if i > 20000:
            # optimization hoping there will be something else with smaller primes
            return -1
        if n % i == 0:
            return i
    return -1

# number is a string, base the the value of number in that base
def value_in_base(base, number):
    if len(number) == 0:
        return 0
    return int(number[-1]) + base * value_in_base(base, number[:-1])


def coin_jam_divisors(candidate):
    divisors = []
    for base in xrange(2, 11):
        # print "computing value in base", base
        value = value_in_base(base, candidate)
        # print "checking if prime", value
        divisor = is_prime(value)
        if divisor == -1:
            return None
        else:
            divisors.append(divisor)
    return divisors


def get_middle_num(length):
    for item in itertools.product(['0', '1'], repeat=length):
        yield ''.join(item)


def generate_candidate(length):
    for inside in get_middle_num(length - 2):
        number_as_list = ['1', inside, '1']
        yield ''.join(number_as_list)


def compute_solutions(string_length, num_solutions_required):
    solutions = []
    for candidate in generate_candidate(string_length):
        # print candidate
        divisors = coin_jam_divisors(candidate)
        if divisors is not None:
            solutions.append((candidate, divisors))
            # print "\n******Solutions found:", len(solutions)
            if len(solutions) == num_solutions_required:
                return solutions


def main(filename):
    with open(filename) as f:
        num_entries = int(f.readline())
        for i in range(num_entries):
            n, j = f.readline().strip().split()
            j = int(j)
            n = int(n)
            solutions = compute_solutions(n, j)
            print "Case #" + str((i + 1)) + ": "
            for solution in solutions:
                value, divisors = solution
                print value, ' '.join(str(e) for e in divisors)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You should provide the input file name"
    else:
        main(sys.argv[1])
