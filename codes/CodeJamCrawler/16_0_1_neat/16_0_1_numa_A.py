from sets import Set

def solve(x):
    if x == 0:
        return "INSOMNIA"
    s = Set([])
    cur = x
    while True:
        for c in str(cur):
            s.add(int(c))
        if len(s) == 10:
            return str(cur)
        cur += x

if __name__ == '__main__':
    N = int(input())
    for i in range(N):
        print "Case #" + str(i + 1) + ": " + solve(int(input()))
