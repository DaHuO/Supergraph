import sys

test_path = 'B-test.in'


def main(input_path=test_path):
    with open(input_path) as f:
        T = int(f.readline().strip())
        for t in range(T):
            S = list(f.readline().strip())
            happy = [s == '+' for s in S]
            print("Case #{0}: {1}".format(t + 1, solve(happy)))


def solve(happy):
    nf = 0
    while not all(happy):
        i = 1
        while i < len(happy) and happy[i] == happy[i - 1]:
            i += 1
        # if i == len(happy):
        #     return nf
        happy = flip(happy, i)
        nf += 1
    return nf
    pass


def flip(arr, i):
    return [not x for ix, x in enumerate(arr) if ix < i][::-1] + arr[i:]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
