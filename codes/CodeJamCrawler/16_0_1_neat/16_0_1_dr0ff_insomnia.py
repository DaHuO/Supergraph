import sys


def solve(num):
    curr = num
    if not num:
        return 'INSOMNIA'
    seen = set()
    for digit in str(num):
        seen.add(digit)
    while len(seen) < 10:
        curr += num
        for digit in str(curr):
            seen.add(digit)
    return curr


def main():
    answer = "Case #{0}: {1}"
    test_num = int(sys.stdin.readline())
    for tnum in range(test_num):
        num = int(sys.stdin.readline())
        ans = solve(num)
        print(answer.format(tnum + 1, ans))


if __name__ == '__main__':
    main()
