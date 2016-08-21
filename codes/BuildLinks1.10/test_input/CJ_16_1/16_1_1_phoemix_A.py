t = int(raw_input())

for case in range(1, t + 1):
    s = raw_input()
    last = s[0]
    r = s[0]

    for c in s[1:]:
        if c >= r:
            last = c + last
            r = c
        else:
            last = last + c


    print "Case #%d: %s" %(case, last)