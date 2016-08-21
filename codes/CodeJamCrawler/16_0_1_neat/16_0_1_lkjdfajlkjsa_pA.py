import itertools


def digitsInNumber(n):
    return set(str(n))


def lastNumber(N):
    if N == 0:
        return "INSOMNIA"
    else:
        digits = set()
        n = N
        for i in itertools.count(1):
            digits.update(set(str(n)))
            if len(digits) == 10:
                return n
            else:
                n += N


T = int(input())

#maxI = 0
#maxN = None

for t in range(1, T + 1):
    N = int(input())
    lastNum = lastNumber(N)
    print("Case #{}: {}".format(t, lastNum))

    #if type(lastNum) == int and (lastNum // N) > maxI:
    #    maxI = lastNum // N
    #    maxN = N


# print(maxN, maxI)
