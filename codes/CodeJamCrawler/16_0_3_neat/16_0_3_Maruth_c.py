import itertools
from math import sqrt

def isPrime(N):
    global prime
    global comp

    if N in prime:
        return (True,)
    if N in comp:
        return (False, comp[N])

    a = int(sqrt(N)) + 2

    for i in range(2,a):

        if N % i == 0:

            comp[N] = i
            return (False, i)

    prime[N] = None
    return (True,)

def checkInBases(s):

    li = []

    for base in range(2,11):
        n = 0

        for i in range(len(s)):
            if int(s[i]):
                n += pow(base, i)

        a = isPrime(n)
        if not a[0]:
            li.append(a[1])

    return li


def main():
    k = 0
    for y in range(int(input())):
        print("Case #%d:" % (y+1))
        N, J = map(int, input().split())
        sts = tuple("".join(seq) for seq in itertools.product("01", repeat=N))

        for i in sts:

            if k == J:
                break

            if (int(i[0]) == 1 and int(i[len(i) - 1]) == 1) and not isPrime(int(i))[0]:

                b = checkInBases(i[::-1])
                if len(b) == 9:
                    k += 1
                    print("%s %d %d %d %d %d %d %d %d %d" % (i, b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]))


if __name__ == '__main__':
    prime = {}
    comp = {}
    main()
