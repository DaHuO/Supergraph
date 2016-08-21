def get_start(n, base):
    return base ** (n-1) + 1


limited_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def get_min_divisor(x):
    # Based off of http://stackoverflow.com/a/27946768/1226799
    if x < 2:
        return x
    for number in limited_primes:
        if not x % number:
            return number
    return x


def convert_to_base(x, base):
    """
    Determine @p x in binary and convert it to a number in base @p base.
    """
    exp = 0
    result = 0
    while x > 0:
        if x % 2:
            result += base ** exp
        x = x/2
        exp += 1
    return result


def solve(instance):
    result = ''
    n, j = instance.split()
    n, j = int(n), int(j)
    start_base = 2
    max_base = 10

    max_val = start_base ** n - 1
    min_val = get_start(n, start_base)
    x = max_val
    while x >= min_val:
        if j == 0:
            break
        divisor = get_min_divisor(x)
        if divisor != x:
            divisors = [divisor]
            # Check if it is prime in other bases.
            for base in xrange(start_base + 1, max_base + 1):
                num_in_base = convert_to_base(x, base)
                divisor = get_min_divisor(num_in_base)
                if divisor == num_in_base:
                    break
                else:
                    divisors.append(divisor)
            else:
                print "{:b}/{} is a jamcoin".format(x, x)
                result += '{:b} {}\n'.format(x, ' '.join(map(str, divisors)))
                j -= 1

        x -= start_base

    return result


def read_input():
    with open('C-large.in') as f:
        lines = list(f)
    # Skip the number of examples.
    instances = lines[1:]
    with open('output.txt', 'w') as f:
        solns = []
        for case, sol in enumerate(map(solve, instances), 1):
            soln = "Case #%(case)s:\n%(sol)s" % vars()
            solns.append(soln)
        # Writing output all at once is faster when the list is small.
        f.write('\n'.join(solns))

read_input()
