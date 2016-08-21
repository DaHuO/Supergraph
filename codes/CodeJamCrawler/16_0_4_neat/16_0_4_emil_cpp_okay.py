T = int(input())
for t in range(T):
    a, b, c = list(map(int, input().split()))
    print ('Case #%s: %s' % (t+1, ' '.join(map(str, range(1, a+1)))))
