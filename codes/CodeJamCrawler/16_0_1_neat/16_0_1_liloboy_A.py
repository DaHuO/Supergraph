
def solve(x):
    #print 'solve: ' + str(x)
    s = set([str(i) for i in range(10)])

    index = 1
    while len(s) > 0:
        #print 's: ' + str(s)
        count = x * index
        index += 1
        #print 'new count: ' + str(count)
        if count == x * index:
            return 'INSOMNIA'
        chars = list(str(count))
        #print 'chars: ' + str(chars)
        for c in chars:
            #print 'c: ' + c
            if c in s:
                #print 'remove'
                s.remove(c)
    return str(count)

fi = open("input.txt", "r")
N = int(fi.readline())

fo = open("output.txt", "w")

for i in xrange(N):
    inp = int(fi.readline())
    fo.write('Case #%d: %s\n' % (i+1, solve(inp)))
    
fi.close()
fo.close()
