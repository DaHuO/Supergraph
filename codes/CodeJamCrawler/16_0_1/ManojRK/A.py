from itertools import count


def main(tc):
    n = int(input())
    if not n:
        print("Case #{}: INSOMNIA".format(tc))
        return
    digits = {str(i) for i in range(10)}
    for i in count(n, n):
        digits -= set(str(i))
        if not digits:
            print("Case #{}:".format(tc), i)
            return


for tc in range(1, int(input()) + 1):
    main(tc)