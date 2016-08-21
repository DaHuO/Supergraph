def testcase(ind): # Rank and File
    N = int( raw_input() )
    lists = []
    for _ in xrange(2*N-1):
        lists.extend( map(int, raw_input().split()) )
    from collections import Counter
    ctr = Counter(lists)
    res = sorted( filter(lambda k: ctr[k]%2==1, ctr) )
    print 'Case #%d: %s' % ( ind, ' '.join(map(str,res)) )

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)
