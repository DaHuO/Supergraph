# 3 6 9 2 5 8 1 4 7 0
# 7 4 1 8 5 2 9 6 3 0
# 1 2 3 4 5 6 7 8 9 0
# 9 8 7 6 5 4 3 2 1 0

t = input()
bm = [True] * 10
for kei in xrange(1,t+1):
    n = input()
    if n == 0:
        sol = 'INSOMNIA'
    else:
        for i in xrange(10):
            bm[i] = True
        c = 10
        x = 0
        while True:
            x += n
            y = x
            while y != 0:
                d = y%10
                if bm[d]:
                    bm[d] = False
                    c -= 1
                y /= 10
            if c == 0:
                break
        sol = x

    print "Case #{}: {}".format(kei, sol)