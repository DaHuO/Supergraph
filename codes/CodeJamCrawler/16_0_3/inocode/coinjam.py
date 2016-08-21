from math import sqrt

def perms(n):
    if n == 0:
        return [[]]
    else:
        ps = []
        smallPs = perms(n-1)
        for smallP in smallPs:
            ps.append([0] + smallP)
            ps.append([1] + smallP)
        return ps

def divisor(n):

    sqrtN = int(sqrt(n))

    for i in range(2, sqrtN):
        if n % i == 0:
            return i
    return 1

def toMaybeCoinjam(p):
    return "".join( map(str, [1] + p + [1]) )

def coinjamDivisors(maybeCoinjam):

    divisors = []

    for b in range(2,10+1):

        num = int(maybeCoinjam,b)

        d = divisor(num)

        if d == 1:
            return []

        divisors.append(d)

    return divisors

def main():

    N = 16
    J = 50

    coinjams = []

    revPerms = perms(N-2)
    revPerms.reverse()
    maybeCoinjams = [ toMaybeCoinjam(p) for p in revPerms ]

    for maybeCoinjam in maybeCoinjams:

        #print("checking", maybeCoinjam, end=" ")

        ds = coinjamDivisors(maybeCoinjam)

        if len(ds) > 0:
            #print(ds)
            coinjams.append((maybeCoinjam,ds))

        if len(coinjams) == J:
            break

    print("Case #1:")
    for (coinjam,divisors) in coinjams:
        print(coinjam, end=" ")
        for d in divisors: print(d, end=" ")
        print()

if __name__ == "__main__":
    main()
