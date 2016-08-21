t = int(raw_input())

for i in xrange(1, t + 1):
    s = raw_input()
    times = 0
    if s[-1] == '-':
        times = 1
    current = s[0]
    for next in s[1:]:
        if next == current:
            continue
        else:
            current = next
            times += 1
            
    print "Case #{}: {}".format(i, times)

