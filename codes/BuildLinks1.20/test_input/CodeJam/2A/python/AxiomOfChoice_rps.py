solns = {0: {
    (1, 0, 0): 'R',
    (0, 1, 0): 'P',
    (0, 0, 1): 'S'
}}

N = 12


def gen():
    for i in range(N):
        solns[i + 1] = {}
        for a in solns[i]:
            for b in solns[i]:
                if solns[i][a] < solns[i][b]:
                    solns[i + 1][a[0] + b[0], a[1] + b[1], a[2] + b[2]] = solns[i][a] + solns[i][b]


def main():
    gen()
    for i in range(int(input())):
        n, r, p, s = map(int, input().split())
        print('Case #{}: {}'.format(
            i + 1,
            solns[n].get((r, p, s), 'IMPOSSIBLE')
        ))


if __name__ == '__main__':
    main()
