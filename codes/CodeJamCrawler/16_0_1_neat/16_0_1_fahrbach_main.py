def main():
    T = int(raw_input())
    for t in range(T):
        n = int(raw_input())
        ans = ''
        if n == 0:
            ans = 'INSOMNIA'
        else:
            S = set([c for c in str(n)])
            m = n
            for i in range(0, 10**5):
                if len(S) == 10:
                    ans = str(m)
                    break
                m += n
                for c in str(m):
                    S.add(c)
        print 'Case #%d: %s' % (t+1, ans)

main()
