
def fixList(s):
    flips = 1
    length = len(s)
    if s[0] == 1:
        flips = 2
        i = 0
        while s[i] == s[0]:
            i += 1
        for j in xrange(i):
            s[j] = 0
    s.reverse()
    for j in xrange(length):
        s[j] = (s[j] + 1)%2
    if length == sum(s): #we are done, list is completed
        return flips
    #there exists a negative val
    i = length-1
    while s[i] == 1:
        i -= 1
    return flips + fixList(s[:i+1])

t = int(raw_input())
for j in xrange(1,t+1):
    s = list(raw_input())
    length = len(s)
    num = 0
    newList = [0 for x in xrange(length)]
    for i in xrange(length):
        if s[i] == '+':
            num += 1
            newList[i] = 1
    if num != length:
        i = length-1
        while newList[i] == 1:
            i -= 1
        num = fixList(newList[:i+1])
    else:
        num = 0
    print "Case #{}: {}".format(j,num)