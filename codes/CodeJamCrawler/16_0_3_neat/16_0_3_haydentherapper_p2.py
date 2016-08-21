import math
import itertools

# From http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

# Based on response in:
#http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def generate_divisors(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i

print("Case #1:")
overall_count = 0
N = 16
J = 50
nums = list(range(2**(N-2)))
for n in nums:
    n = bin(n)[2:].zfill(14)
    n = '1' + n + '1'
    all_divs = []
    for base in range(2, 11):
        new_n = int(n, base)
        if not isprime(new_n):
            divs = generate_divisors(new_n)
            divs = list(itertools.islice(divs, 2))
            all_divs.append(str(divs[1]))
    if len(all_divs) == 9:
        print(n, ' '.join(all_divs))
        overall_count += 1
    if overall_count == J:
        break


