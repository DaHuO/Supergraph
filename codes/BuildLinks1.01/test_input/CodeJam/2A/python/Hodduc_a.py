def main():
    T = input()

    for t in range(1, T+1):

        N, R, P, S = map(int, raw_input().split())

        def tr(n, ch):
            if n == 0:
                return ch

            if ch == 'P':
                l, r = tr(n-1, 'P'), tr(n-1, 'R')
            elif ch == 'R':
                l, r = tr(n-1, 'S'), tr(n-1, 'R')
            else:
                l, r = tr(n-1, 'P'), tr(n-1, 'S')

            if l > r:
                return r + l
            else:
                return l + r

        ans = None

        x = tr(N, 'P')
        if x.count('P') == P and x.count('R') == R and x.count('S') == S:
            ans = x

        x = tr(N, 'R')
        if x.count('P') == P and x.count('R') == R and x.count('S') == S:
            if ans is None or ans > x:
                ans = x

        x = tr(N, 'S')
        if x.count('P') == P and x.count('R') == R and x.count('S') == S:
            if ans is None or ans > x:
                ans = x

        if ans == None:
            print "Case #%d: IMPOSSIBLE" % t
        else:
            print "Case #%d: %s" % (t, ans)

main()
