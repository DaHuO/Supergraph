def go(N):
    step = N
    digits = set(str(N))
    while len(digits) != 10:
        N += step
        digits.update(str(N))
    return N

if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        print("Case #{}: {}".format(t, "INSOMNIA" if N == 0 else go(N)))
