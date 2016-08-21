import sys


def solve(n):
    
    if n <= 0:
        return 0
    
    seen = [False] * 10
    m = 0
    while not all(seen):
        m += n
        x = m
        while x > 0:
            seen[x % 10] = True
            x //= 10
    return m


if (__name__ == '__main__') and (len(sys.argv) == 3):
    with open(sys.argv[1]) as fin, open(sys.argv[2], 'w') as fout:
        numCases = int(fin.readline().strip())
        for c in range(numCases):
            n = int(fin.readline().strip())
            m = solve(n)
            fout.write('Case #{}: {}\n'.format(c+1, m if m > 0 else 'INSOMNIA'))