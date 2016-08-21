import sys
sys.stdout = open("output.txt", "w+")


N = 16
J = 50


def get_primes(n):
    # http://stackoverflow.com/a/2068548/287255
    " Returns  a list of primes < n "
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def get_divisor(bits, base):
    number = int(bits, base)

    for divisor in primes:
        if number <= divisor:
            break

        if number % divisor == 0:
            return divisor

    return 0


def jamcoin_detection(bits):
    result = []
    for base in range(2, 11):
        divisor = get_divisor(bits, base)
        if divisor == 0:
            return (False, [])
        result.append(str(divisor))

    return (True, result)


primes = get_primes(int(int("1" * N) ** 0.5))

print "Case #1:"
for i in xrange(2 ** (N - 2)):
    bits = "1" + ("{0:0%db}" % (N - 2)).format(i) + "1"
    if len(bits) != N or J <= 0:
        break

    detected, divisors = jamcoin_detection(bits)
    if not detected:
        continue

    print bits, " ".join(divisors)
    J -= 1
