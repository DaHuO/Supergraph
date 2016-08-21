def solve(n):
    if n == 0: return "INSOMNIA"
    i, N, digits= 1, n, []
    while True:
        digits += [int(m) for m in str(n) if not int(m) in digits]
        if all(k in digits for k in range(10)):
            return n
        n += N
        i += 1

def a():
    T = int(raw_input())
    for t in range(1,T+1):
        N = int(raw_input())
        print "Case #{}:".format(t), solve(N)

if __name__ == '__main__':
    a()
