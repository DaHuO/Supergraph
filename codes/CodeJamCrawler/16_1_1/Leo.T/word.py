import sys

test_path = 'A-test.in'


def main(input_path=test_path):
    with open(input_path) as f:
        T = int(f.readline().strip())
        for t in range(T):
            S = f.readline().strip()
            ans = solve(S)
            print("Case #{0}: {1}".format(t + 1, ans))


def solve(S):
    res = S[0]
    S = S[1:]
    for s in S:
        if s >= res[0]:
            res = s + res
        else:
            res = res + s
    return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
