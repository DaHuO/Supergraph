from collections import deque
for t in xrange(input()):
    s = raw_input()
    d=deque()
    d.append(s[0])
    for ch in s[1::]:
        if ord(ch) >= ord(d[0]):
            d.appendleft(ch)
        else:
            d.append(ch)

    print 'Case #%d:' % (t + 1), "".join(d)
