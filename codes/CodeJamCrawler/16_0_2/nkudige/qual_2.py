def flipem(ip):
    flips = 0

    current = ip[0]
    for i in xrange(1, len(ip)):
        if ip[i] == current:
            pass
        else:
            current = ip[i]
            flips += 1

    if current == 0:
        flips += 1

    return flips


T = int(raw_input())

for i in xrange(1, T+1):
    ip = map(int, list(raw_input().replace('+', '1').replace('-', '0')))
    print 'Case #%d: %s' % (i, flipem(ip))