import fileinput
import itertools


def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return True

def solve(N, J):
    counter = 0
    for nums in itertools.product(["0", "1"], repeat=N-2):
        string = "1"
        for n in nums:
            string += n
        string +="1"
        foundPrime = False
        baseFactors = []
        for base in range(2,11):
            n = int(string, base)
            isPrime = isprime(n)
            if isPrime is True:
                foundPrime = True
                break
            else:
                baseFactors.append(str(isPrime))
        if not foundPrime:
            print string, " ".join(baseFactors)
            counter += 1
            if counter == J:
                return

print "Case #1:"
solve(16,50)

# for i, line in enumerate(fileinput.input()):
#     if i == 0:
#         continue
#     N, J = map(int, line.strip().split(" "))
#     res = solve(N, J)
#     print "Case #%d: %s" % (i, res)
