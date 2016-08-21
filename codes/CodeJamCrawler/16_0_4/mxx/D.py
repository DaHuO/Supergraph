def testcase(ind): # Fractiles
    K, C, S = map(int, raw_input().split())
    seg_len = K**(C-1)
    res = ''
    for i in xrange(S): 
        res += str(i*seg_len+1)+' '
    print 'Case #%d: %s' % (ind, res)

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)
