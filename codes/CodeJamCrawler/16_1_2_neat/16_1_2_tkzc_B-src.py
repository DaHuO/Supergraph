from collections import Counter


def find_missing(grid):
    c = Counter(grid)
    missing_line = []
    for height in c:
        if c[height] % 2 == 1:
            missing_line.append(height)
    missing_line = sorted(missing_line, key=int)
    return map(str, missing_line)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        grid = []
        n = int(input())
        for k in range(2 * n - 1):
            line = [int(s) for s in input().split(' ')]
            grid += line
        missing_line = find_missing(grid)
        print('Case #{}: {}'.format(i + 1, ' '.join(missing_line)))
