import sys


def teardown(n):
    got = set()

    while n > 0:
        got.add(n % 10)
        n //= 10

    return got


def solve(quiz):
    if quiz == 0:
        return "INSOMNIA"

    num = quiz
    seen = set()
    multiplier = 1

    while True:
        seen.update(teardown(num))
        if len(seen) == 10:
            return num

        multiplier += 1
        num += quiz


def main(fn):
    with open(fn) as fp:
        count = int(fp.readline().strip())

        for idx in range(1, count+1):
            print("Case #%d: %s" % (
                idx,
                solve(int(fp.readline().strip()))
            ))


if __name__ == "__main__":
    main(sys.argv[1])

