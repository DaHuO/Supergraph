import math

INPUT = "3-large"

f = open('%s.in' % INPUT, 'r')
o = open('%s.out' % INPUT, 'w')

T = int(f.readline().strip())
BASE_RANGE = range(2, 11)


def to_base_2_str(n):
    return str(bin(n)[2:])


def from_base(st, n):
    _sum = 0
    current_power = 0
    for c in reversed(list(st)):
        _sum += int(c) * (n ** current_power)
        current_power += 1
    return _sum


def get_all_bases(st):
    return [from_base(st, base) for base in BASE_RANGE]


def get_first_divisor(n):
    if n % 2 == 0:
        return 2

    # optimization for fast coin finding
    # assume that it is prime if we cant find it in first 5000 divisors
    # this param can be tuned
    max_try_count = 5000
    for i in xrange(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return i
        max_try_count -= 1
        if max_try_count == 0:
            return 0

    return 0


def solve(binary_length, cnt):
    base_str = '1' + '0' * (binary_length -2) + '1'
    base_int = from_base(base_str, 2)

    for candidate in xrange(base_int, base_int*2 - 1, 2):
        candidate_coin = to_base_2_str(candidate)

        valid_candidate = True
        divisors = []
        all_bases = get_all_bases(candidate_coin)
        for base in all_bases:
            div = get_first_divisor(base)
            if div == 0:
                valid_candidate = False
                break
            else:
                divisors.append(str(div))

        if valid_candidate:
            print all_bases
            yield " ".join([candidate_coin] + divisors)
            cnt -= 1
        if cnt <= 0:
            break

for t in xrange(T):
    total = 0
    inverted = False
    b_length, coin_cnt = f.readline().strip().split()

    s = "Case #%d:\n" % (t + 1)
    print s
    o.write(s)

    for a in solve(int(b_length), int(coin_cnt)):
        print a
        s = "{0}\n".format(a)
        o.write(s)

f.close()
o.close()
