IN = 'input.txt'
OUT = 'output.txt'


def group(xs):
    if len(xs) == 0:
        return []

    res = [[xs[0]]]

    for x in xs[1:]:
        if x == res[-1][-1]:
            res[-1].append(x)
        else:
            res.append([x])

    return res


def sol(line):
    return str(len(group(line)) - (1 if line[-1] == '+' else 0))


def main():
    with open(IN, 'r') as f, open(OUT, 'w') as g:
        t = int(f.readline())
        for i in range(t):
            g.write('Case #{}: '.format(i + 1))
            g.write(sol(f.readline().strip()))
            g.write('\n')


if __name__ == '__main__':
    main()
