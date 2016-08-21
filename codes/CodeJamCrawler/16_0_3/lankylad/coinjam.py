import itertools


def find_divisor(x):
    i = 2
    while i*i < x:
        if not x % i:
            return i
        i += 1
    return 0

def main():
    raw_input()
    print "Case #1:"
    N, J = [int(c) for c in raw_input().split(' ')]
    for sn in ("{0:b}".format(b).zfill(N) for b in xrange(2**(N-1)+1,2**N,2)):
        divisors = []
        for i in xrange(2, 11):
            x = int(''.join(sn), i)
            d = find_divisor(x)
            if d == 0:
                break
            divisors.append(d)
        if len(divisors) == 9:
            print "{} {}".format(''.join(sn), ' '.join(str(k) for k in divisors))
            J -= 1
            if J == 0:
                return
    return

if __name__ == '__main__':
    main()