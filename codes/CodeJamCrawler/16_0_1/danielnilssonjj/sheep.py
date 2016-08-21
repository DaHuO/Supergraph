import sys

def solve_file(filen):
    f = open(filen + '.in', 'r')
    T = int(f.readline())
    print(T)

    ans = ""

    for i in range(1, T+1):
        n = int(f.readline())
        nans = solve_N(n)
        ans += "Case #%d: %s\n" % (i, nans)

    f = open(filen + '.out', 'w')
    f.write(ans)

def solve_N(N):
    if N == 0:
        return 'INSOMNIA'

    l = [0 for i in range(10)]
    Nc = 0

    while sum(l) < 10:
        Nc += N
        d = digits(Nc)
        for dd in d:
            l[dd] = 1

    return Nc

def digits(n):
    d = []
    while n > 0:
        d.append(n%10)
        n //= 10
    return d

if __name__ == '__main__':
    for filen in sys.argv[1:]:
        solve_file(filen)