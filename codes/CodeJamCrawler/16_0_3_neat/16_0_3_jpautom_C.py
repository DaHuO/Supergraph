
def multmod(p, q, m):
    return ((p % m) * (q % m)) % m

def addmod(p, q, m):
    return ((p % m) + (q % m)) % m


def is_divisible(binary, divisor, base):
    res = 0
    power = 1
    i = 0
    while 1 << i <= binary:
        if (1 << i) & binary:
            res = addmod(res, power, divisor)
            # print(binary, divisor, base, i, power, res)
        power = multmod(power, base, divisor)
        i += 1
    return res == 0


def solve(N, J):
    generated = 0
    n = (1 << N-1) + 1

    while generated < J:
        divisors = []
        for base in range(2, 11):
            valid = False
            for divisor in [2, 3, 5, 7, 11]:
                if is_divisible(n, divisor, base):
                    divisors.append(divisor)
                    valid = True
                    break
            if not valid:
                break
        #print len(divisors), divisors
        if len(divisors) == 9:
            print '{:b} {}'.format(n, ' '.join([str(i) for i in divisors]))
            generated += 1
        n += 2


if __name__ == '__main__':
    import sys

    T = int(sys.stdin.readline()) # 1

    for case in range(T):
        N, J = [int(w) for w in sys.stdin.readline().split()] # 16, 32
        print 'Case #{}: '.format(case+1)
        solve(N, J)
