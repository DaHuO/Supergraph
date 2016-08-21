def solve(N):
    if N == 0: return "INSOMNIA"
    x = N
    missing = set(range(10))
    while missing:
        y = x
        while missing and y > 0:
            d = y % 10
            y //= 10
            missing.discard(d)
        x += N
    return x - N

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        print ("Case #%d: %s" % (t, solve(N)))
