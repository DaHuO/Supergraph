t = int(raw_input())
for i in range(t):
    k, c, s = raw_input().split(" ")
    k, c, s = int(k), int(c), int(s)
    ret = ' '.join('{}'.format(1 + j * k ** (c - 1)) for j in range(k))
    print "Case #{}: {}".format(i + 1, ret)
