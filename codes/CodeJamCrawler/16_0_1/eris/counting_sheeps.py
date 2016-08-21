import os
import sys


def task(N):
    if N == 0:
        return 'INSOMNIA'
    nums, sum, i = set(), N, 1
    while True:
        nums.update([x for x in str(sum)])
        if len(nums) == 10:
            return sum
        sum += N


def main():
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()

    T = int(lines[0])
    res = ''
    for i in range(1, T + 1):
        res += 'Case #%d: %s\n' % (i, task(int(lines[i])))

    with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as f:
        f.write(res)

if __name__ == '__main__':
    main()
