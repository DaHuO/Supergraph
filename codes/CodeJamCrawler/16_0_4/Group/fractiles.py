def solve(K, C, S):
    ans = range(1, S+1)
    return ' '.join(map(str, ans))

if __name__ == "__main__":
    import fileinput

    f = fileinput.input()

    T = int(f.readline())

    for t in range(1, T + 1):
        K, C, S = map(int, f.readline().split())
        print("Case #%i: %s" % (t, solve(K, C, S)))
