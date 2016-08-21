def testcase(ind): # The Last Word
    S = raw_input()
    res = ''
    for c in S:
        if len(res)>0 and res[0]<=c:
            res = c + res
        else: 
            res = res + c
    print 'Case #%d: %s' % (ind, res)

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)
