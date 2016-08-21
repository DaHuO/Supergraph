P = {}

def get(X):
    i = 2
    for it in range(10000):
        if i * i > X:
            break
        if X % i == 0:
            return i
        i += 1
    return -1

def solve():
    tot = 0
    N = 14
    print "Case #1:"
    for B in range(2, 11):
        P[B] = {}
        P[B][0] = 1
        for i in range(1, 35):
            P[B][i] = P[B][i - 1] * B
    for i in range(1 << N):
        M = i
        if (M & (1 << 0)) == 0:
            continue
        M |= 1 << 31
        ok = True
        ss = ""
        f = {}
        for B in range(2, 11):
            X = 0
            for j in range(32):
                if (M & (1 << j)) != 0:
                    X += P[B][j]
            Z = get(X)
            if Z == -1:
                ok = False
                break
            f[B] = Z
        if ok == True:
            ss = ""
            for j in range(32):
                if (M & (1 << (31 - j))) == 0:
                    ss += '0'
                else:
                    ss += '1'
            for j in range(2, 11):
                ss += ' '
                ss += str(f[j])
            tot += 1
            print ss
        if tot == 500:
            break

solve()
