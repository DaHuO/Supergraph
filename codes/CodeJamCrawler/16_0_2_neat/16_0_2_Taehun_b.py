t = int(raw_input().strip())

for i in xrange(t):
    s = raw_input().strip()

    count = 0
    ii = 0
    while ii < len(s):
        rc = s[ii]
        j = ii + 1
        while j < len(s):
            if s[j] != rc:
                break
            j = j + 1
        ii = j
        count = count + 1
    if rc == '+':
        count = count - 1
    print "Case #" + str(i + 1) + ": " + str(count)
