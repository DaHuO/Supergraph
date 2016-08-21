from math import sqrt

T = int(input())

def get_a_divider(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    for i in xrange(5, int(sqrt(n)+1)):
        if n % i == 0:
            return i
    return -1

for i in range(T):
    N, J = map(int, raw_input().split())

    print "Case #1: "
    count = 0
    for j in xrange(2**14):
        s = '1'+"{0:014b}".format(j)+'1'

        x = []
        for j in range(2, 11):
            d = get_a_divider(int(s, j))
            if d == -1:
                break
            x.append(d)
        if len(x) != 9:
            continue
        print "%s %s" % (s, " ".join(map(str, x)))
        count += 1

        if count == J:
            break


