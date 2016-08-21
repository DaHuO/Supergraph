t = int(raw_input())
inputs = []

for x in range(t):
    inputs.append(raw_input())


def findBadPos(s):
    lastBadPos = len(s)
    counter = 0
    for i in s:
        if i == -1:
            # print "bad"
            lastBadPos = counter
        counter += 1
    return lastBadPos

for n, x in enumerate(inputs):
    s = []
    ans = 0
    for el in x:
        if el == '-':
            s.append(-1)
        elif el == '+':
            s.append(1)
    # print s

    lastBadPos = findBadPos(s)
    while lastBadPos != len(s):
        ans += 1
        s = s[:lastBadPos+1]
        s = [x*-1 for x in s]
        lastBadPos = findBadPos(s)
        # print s, lastBadPos
        # break
    print "Case #%r: %r" % (n+1, ans)
