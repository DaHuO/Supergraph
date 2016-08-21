def gen_primes():
    prime = [True] * 100007
    primes_ = [2]
    for i in xrange(3, 100007, 2):
        if prime[i]:
            primes_.append(i)
            if i < 10000:
                for j in xrange(i*i, 100007, i):
                    prime[j] = False
    return primes_


def get_divisor(x):
    for i in primes:
        if i >= x:
            return None
        if x % i == 0:
            return i


def check(num):
    for i in xrange(2, 11):
        x = int(num, i)
        divisor = get_divisor(x)
        if divisor is None:
            return False
        divs[i] = str(divisor)
    return True


if __name__ == '__main__':
    ans = []
    primes = gen_primes()
    divs = [None] * 11
    number = 2**31 + 1
    print len(bin(number)) - 2
    t = 500
    while t > 0:
        if check(bin(number)[2:]):
            t -= 1
            ans.append(bin(number)[2:] + ' ' + ' '.join(divs[2:]))
        number += 2
    with open('output3.out', 'w') as f:
        f.write('Case #1:\n')
        f.write('\n'.join(ans))
