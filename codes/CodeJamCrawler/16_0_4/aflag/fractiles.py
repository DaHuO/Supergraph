import sys

def solve(k, c, s):
    if c == 1:
        if s == k:
            return " ".join(str(i) for i in range(1, k + 1))
        return "IMPOSSIBLE"
    elif k == 1:
        if s == 0:
            return "IMPOSSIBLE"
        else:
            return "1"
    else:
        if s < (k-1):
            return "IMPOSSIBLE"
        return " ".join(str(i) for i in range(2, k + 1))


if __name__ == '__main__':
    total = int(sys.stdin.readline().strip())
    for case in range(1, total + 1):
        k, c, s = sys.stdin.readline().strip().split()
        print("Case #{}: {}".format(case, solve(int(k), int(c), int(s))))
