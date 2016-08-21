n = int(raw_input())
for I in range(1,n+1):
    s = raw_input()
    count = 0
    start = len(s)
    for i in range(start-1,-1,-1):
        if s[i] == '-':
            start = i
            break
    if (start == len(s)):
        print "Case #" + str(I) + ": 0"
    else:
        for i in range(start-1, -1,-1):
            if (s[i] != s[i+1]):
                count = count+1
        count = count+1
        print "Case #" + str(I) + ": " + str(count)
