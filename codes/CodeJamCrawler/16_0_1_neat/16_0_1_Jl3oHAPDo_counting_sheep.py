#!python3


def solve(N, a, cN):
    if N == 0:
        return 'INSOMNIA'
    for current_number in str(N):
        if int(current_number) in a:
            try:
                a.remove(int(current_number))
            except:
                pass
    if len(a):
        N = solve(N + cN, a, cN)
    return N


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        N = int(f.readline())
        answer = solve(N, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], N)
        print("Case #{0}: {1}".format(case, answer))