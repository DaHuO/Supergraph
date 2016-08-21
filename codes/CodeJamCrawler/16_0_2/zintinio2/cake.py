from sys import stdin


def flip(ps, n):
    t = ps[:n]
    b = ps[n:]
    tfpd = []
    for n in reversed(t):
        if n == '+':
            tfpd.append('-')
        else:
            tfpd.append('+')
    return ''.join(tfpd) + b


def smile(ps):
    if ps.count('-') == 0:
        return 0
    else:
        hap = -1
        for c in ps:
            if c == '+':
                hap += 1
            else:
                break
        if hap != -1:
            nxt = flip(ps, hap + 1)
        else:
            sad = ps.rfind('-')
            nxt = flip(ps, sad + 1)
        return 1 + smile(nxt)


if __name__ == '__main__':
    T = int(stdin.readline().strip())
    for n in range(T):
        k = smile(stdin.readline().strip())
        print('Case #' + str(n+1) + ": " + str(k))