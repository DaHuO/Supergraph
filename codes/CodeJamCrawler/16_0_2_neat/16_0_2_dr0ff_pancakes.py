import sys


def solve(pks):
    curr = '+'
    flips = 0
    for ptype in reversed(pks):
        if ptype != curr:
            flips += 1
            curr = ptype
    return flips


def main():
    answer = "Case #{0}: {1}"
    test_num = int(sys.stdin.readline())
    for tnum in range(test_num):
        pks = sys.stdin.readline().strip()
        ans = solve(pks)
        print(answer.format(tnum + 1, ans))


if __name__ == '__main__':
    main()
