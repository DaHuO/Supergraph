import sys

def isPrime(number):
    i = 2
    sqr = i * i
    while ( sqr <= number ):
        if ( number % i == 0 ):
            return (False, i)
        i = i + 1
        sqr = i * i
    return (True, i)

def helperBase (number):
    base = 2

    prime_list = []
    base_numbers = [int(number,j) for j in range(2,11)]

    for base_number in base_numbers:
        (is_Prime, prime) = isPrime(base_number)
        if (not is_Prime):
            prime_list.append(prime)

    if ( len(prime_list) == 9 ):
        print number, ' '.join(str(prime_list[i]) for i in xrange(len(prime_list))),
        print
        return True
    return False

if __name__ == '__main__':
    # Input processing
    T = int(raw_input())
    l = raw_input().split()
    length = int(l[0])
    numlines = int(l[1])

    print("Case #1:")

    # Form the start and end strings
    start = ''.join('0' for i in xrange(length - 2))
    start = '0b1' + start + '1';
    end = ''.join('1' for i in xrange(length));
    end = '0b' + end

    start = int(start, 2)
    end = int(end, 2)

    global primes
    count = 0

    while ( start <= end and count != numlines):
        if ( helperBase(str(bin(start)[2:])) ):
            count = count + 1
        start = start + 2
