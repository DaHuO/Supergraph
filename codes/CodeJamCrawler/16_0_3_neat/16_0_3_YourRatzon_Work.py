def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite

def is_prime(n, _precision_for_huge_n=40):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


def sieve(limit):
    yield 2
    if limit < 3: return
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    for i in range(lmtbf + 1):
        if buf[i]: yield (i + i + 3)

def from_base_to_decimal(num, base):
    res = 0
    mult = 1
    while num:
        res += mult * (num%10)
        num//=10
        mult *= base
    return res

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

fin = open(r'C:\Users\Yechiel\Downloads\c.in', 'r+')
fout = open(r'C:\Users\Yechiel\Downloads\c.out', 'w+')

line = fin.read().split()
T = int(line[0])
N = int(line[1])
J = int(line[2])
the_num = int('1' + ('0'*(N-2)) + '1')
curr_num = from_base_to_decimal(int(the_num), 2)
primes_list = list(sieve(int(1e7)))

fout.write('Case #1:\n')
while J:
    good = True
    divs = []
    curr_nums = []
    for i in range(2, 11):
        curr_num = from_base_to_decimal(the_num,i)
        curr_nums.append(curr_num)
        if is_prime(curr_num):
            good = False
            break
    if good:
        for curr_num in curr_nums:
            for prime in (primes_list):
                if prime*prime > curr_num:
                    good = False
                    break
                if curr_num % prime == 0:
                    divs.append(str(prime))
                    break

            if not good:
                break
    if good:
        fout.write('{} {}\n'.format(the_num,' '.join(divs)))
        J -= 1
    the_num = int('{0:b}'.format(from_base_to_decimal(int(the_num), 2) + 2))

fin.close()
fout.close()

