ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve(N, P):
    print N, P
    ans = ''
    d = dict(zip(ABC[:len(P)], P))
    mx = max(d.values())
    nr = 2
    while mx > 0:
        mx = max(d.values())
        if mx == 1:
            if len(d.keys()) == 2:
                nr = 2
            else:
                nr = 1
        for i in range(nr):
            for k in d.keys():
                mx = max(d.values())
                if d[k] == mx:
                    v = mx
                    ans += k
                    d[k] -= 1
                    if d[k] == 0:
                        d.pop(k, None)
                    break
        if len(d.keys()) == 0:
            break
        ans += ' '
    return ans.strip()


def main():
    f_in = open('A-large.in', 'r')
    # f_in = open('A-large-test.in', 'r')
    f_out = open('A-large.out', 'w')
    T = int(f_in.readline())
    for i in range(T):
        N = int(f_in.readline())
        P = [int(l) for l in f_in.readline().split()]
        s = "Case #{}: {}\n".format(i+1, solve(N, P))
        print s
        f_out.write(s)
    f_in.close()
    f_out.close()

if __name__ == '__main__':
    main()
