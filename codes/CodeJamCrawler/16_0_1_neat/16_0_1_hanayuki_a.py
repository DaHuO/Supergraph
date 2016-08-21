import sys

T = int(raw_input())

for t in range(1, T+1):
    N = int(raw_input())

    if N == 0:
        print 'Case #%d: INSOMNIA' % (t)
        continue

    num = N
    digits = map(str, range(10))
    while True:
        for c in str(num):
            if c in digits:
                digits.remove(c)
        if digits == []: break

        num += N


    print 'Case #%d: %d' % (t, num)
