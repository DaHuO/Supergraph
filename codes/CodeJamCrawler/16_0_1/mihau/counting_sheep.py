MAX_N_MULT = 101


def digits(N):
    ret = set()
    if N == 0: return [0]
    while N != 0:
        ret.add(N % 10)
        N //= 10
    return ret


def solve(N):
    numberz_now = set()
    for i in range(1, MAX_N_MULT):
        for j in digits(i * N):
            numberz_now.add(j)
        if len(numberz_now) == 10:
            return i * N
    return "INSOMNIA"


if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        N = int(input())
        print("Case #{0}:".format(i + 1), end=" ")
        if N == 0:
            print("INSOMNIA")
        else:
            print(solve(N))
