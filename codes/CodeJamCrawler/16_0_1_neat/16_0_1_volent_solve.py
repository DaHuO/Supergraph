def solve(N):
    digits = set()
    i = 0

    if N == 0:
        return "INSOMNIA"

    while len(digits) < 10:
        i += 1
        digits.update({digit for digit in str(N * i)})

    return N * i


def main():
    T = input()
    for N in xrange(T):
        print "Case #{}: {}".format(N + 1, solve(input()))

if __name__ == "__main__":
    main()
