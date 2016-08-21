n = int(raw_input())

check = [False] * 10

zero = ord('0')

for i in xrange(n):
    start = int(raw_input())
    if start == 0:
        print "Case #{}: INSOMNIA".format(i+1)
    else:
        seen = check[:]
        s = str(start)
        for c in s:
            seen[ord(c) - zero] = True
        current = start
        while(not all(seen)):
            current += start
            s = str(current)
            for c in s:
                seen[ord(c) - zero] = True
        print "Case #{}: {}".format(i+1, s)