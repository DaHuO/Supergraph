import math

T = int(raw_input())
N, J = map(int, raw_input().split())

print 'Case #1:'
cnt = 0
coin = (1 << (N-1)) + 1
while coin < (1 << N):
    failed = False
    divs = [0 for i in xrange(11)]
    for base in range(2, 11):
        num = int(format(coin, 'b'), base)
        d = 2
        while d < 20:
            if num % d == 0:
                divs[base] = d
                break
            d += 1
        if divs[base] == 0:
            failed = True
            break
    if not failed:
        print format(coin, 'b'),
        for base in range(2,10):
            print divs[base],
        print divs[10]
        cnt += 1
        if cnt >= J:
            break
    coin += 2
