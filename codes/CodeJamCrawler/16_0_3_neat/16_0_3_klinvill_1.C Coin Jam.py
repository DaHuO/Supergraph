__author__ = 'Kirby'

# taken from stack overflow, slightly modified for large input
def get_divisor(n):
    if n % 2 == 0:
        return 2

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        # don't bother, the divisor is too large to compute quickly or the number is prime
        if n % divisor == 0:
            return divisor
        elif divisor > 100000:
            return -1
    return -1

def get_divisors(coin):
    divisors = []
    for c in coin:
        divisor = get_divisor(c)
        if divisor == -1:
            return []
        else:
            divisors.append(divisor)
    return divisors


def interpretBases(binString, lowerBase, upperBase):
    return [int(binString, base) for base in range(lowerBase, upperBase+1)]

def jamcoins(bits, count, lowerBase, upperBase):
    # binary strings must start with a 1, end with a 1, and be count bits long
    lowerBin = '1'
    upperBin = '1'
    for n in range(bits-2):
        lowerBin+='0'
        upperBin+='1'
    lowerBin+='1'
    upperBin+='1'

    upper = int(upperBin, 2)

    binString = lowerBin
    binNum = int(binString, 2)

    numElements = len(range(lowerBase, upperBase+1))

    solutions = []
    candidate = interpretBases(binString, lowerBase, upperBase)

    while len(solutions) < count and binNum <= upper:
        divisors = get_divisors(candidate)
        if (len(divisors)) == numElements:
            solutions.append((binString, divisors))

        # the binary strings must end in 1 (be odd)
        binNum += 2
        binString = format(binNum, 'b')
        candidate = interpretBases(binString, lowerBase, upperBase)

    return solutions

def output(solutions):
    with open("results.txt", "w") as f:
        f.write("Case #1:")
        for s in solutions:
            f.write("\n{:s} {:s}".format(s[0]," ".join([str(x) for x in s[1]])))


if __name__ == "__main__":
    with open("test.txt", "r") as f:
        T = int(f.readline())
        N, J = [int(x) for x in f.readline().split()]

        print(T, N, J)
        # T = 1
        # N = 16
        # J = 50

        lowerBase = 2
        upperBase = 10

        output(jamcoins(N, J, lowerBase, upperBase))