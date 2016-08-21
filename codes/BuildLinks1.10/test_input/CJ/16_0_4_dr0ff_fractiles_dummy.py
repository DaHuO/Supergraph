import sys


def solve(orig_size, cx, budget):
    if budget * cx < orig_size:
        return "IMPOSSIBLE"
    else:
        return ' '.join(str(tn + 1) for tn in range(orig_size))

def main():
    answer = "Case #{0}: {1}"
    test_num = int(sys.stdin.readline())
    for tnum in range(test_num):
        orig_size, cx, budget = [int(n) for n in sys.stdin.readline().split()]
        ans = solve(orig_size, cx, budget)
        print(answer.format(tnum + 1, ans))


if __name__ == '__main__':
    main()
