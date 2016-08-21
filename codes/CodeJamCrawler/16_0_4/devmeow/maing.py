from math import sqrt
#from functools import lru_cache

IN = 'input.txt'
OUT = 'output.txt'


def sol(line):
    k, c, s = map(int, line.split())
    c -= 1
    res = []
    for i in range(s):
        res.append(i * k ** c + 1)

    return ' '.join(list(map(str, res)))


def main():
    with open(IN, 'r') as f, open(OUT, 'w') as g:
        t = int(f.readline())
        for i in range(t):
            g.write('Case #{}: '.format(i + 1))
            g.write(sol(f.readline().strip()))
            g.write('\n')


if __name__ == '__main__':
    main()
