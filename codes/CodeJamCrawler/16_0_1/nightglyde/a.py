import sys

cin = sys.stdin.readlines()

complete = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

def countSheep(n):
    if n == 0:
        return "INSOMNIA"
    seen = set()
    i = 1
    while True:
        m = n*i
        while m > 0:
            seen.add(m % 10)
            m //= 10
        if complete <= seen:
            return n*i
        i += 1

T = int(cin[0].strip())
for case in range(1, T+1):
    N = int(cin[case].strip())
    print("Case #{}: {}".format(case, countSheep(N)))

