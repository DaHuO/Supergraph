def readInt(): return int(raw_input())
def readList(): return map(int, raw_input().split(' '))

t = readInt()
for l in xrange(t):
    a = raw_input()
    w = [a[0]]
    a = a[1:]
    b = [0] * 26
    for i in a:
        if ord(i) >= ord(w[0]):
            w = [i] + w
        else:
            w.append(i)

    print "Case #" + str(l+1) + ": " + ''.join(w)