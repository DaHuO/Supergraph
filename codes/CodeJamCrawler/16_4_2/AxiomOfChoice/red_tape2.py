def prob(ps):
    cur = {0: 1}
    for i in range(len(ps)):
        cur = {
            c: ps[i] * cur.get(c - 1, 0) + (1 - ps[i]) * cur.get(c + 1, 0)
            for c in range(-i - 1, i + 2, 2)
        }

    return cur[0]


def work(n, k, ps):
    ps.sort()
    return max(prob(ps[:m] + ps[n - k + m:]) for m in range(k + 1))


def main():
    T = int(input())
    for i in range(T):
        n, k = map(int, input().split())
        ps = list(map(float, input().split()))
        print('Case #{}: {:.7f}'.format(i + 1, work(n, k, ps)))


if __name__ == '__main__':
    main()
