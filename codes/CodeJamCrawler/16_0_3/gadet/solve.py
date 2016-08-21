import sys

data = sys.stdin.read().strip()
n, j = map(int, data.split('\n')[1].strip().split(' '))

start = int("1" + "0"*(n-2) + "1", 2)
end = int("1"*n, 2)
cur = start

# From Stackoverflow: http://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def is_prime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True, None
    if n == 3:
        return True, None
    if n % 2 == 0:
        return False, 2
    if n % 3 == 0:
        return False, 3
    i = 5
    w = 2
    while i * i <= 10000: # stop checking for prime at 10000 and move on, since there are more coin jams later on
        if n % i == 0:
            return False, i
        i += w
        w = 6 - w
    return True, None

def check_coin_jam(num):
    base_2_str = bin(num)[2:]
    is_coin_jam = True
    divisors = []
    for base in range(2, 11):
        base_str = int(base_2_str, base)
        prime, divisor = is_prime(base_str)
        if prime:
            is_coin_jam = False
            break
        else:
            divisors.append(divisor)
    return is_coin_jam, divisors

print "Case #1:"
i = 0
while i < j:
    coin_jam, divisors = check_coin_jam(cur)
    if coin_jam:
        print bin(cur)[2:], ' '.join(map(str, divisors))
        i += 1
    cur += 2
