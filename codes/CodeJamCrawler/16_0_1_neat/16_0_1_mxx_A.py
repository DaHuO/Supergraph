        

def testcase(i): # fall asleep
    digits_seen = set()
    def see_digits(n):
        for d in str(n):
            digits_seen.add(d)
    N = int(raw_input())
    if N==0: 
        print 'Case #%d: %s' % (i, 'INSOMNIA')
        return
    n = N
    cnt = 0
    for cnt in xrange(1000000):
        see_digits(n)
        if len(digits_seen)==10: 
            print 'Case #%d: %s' % (i, str(n))
            return
        n += N
    print 'Case #%d: %s' % (i, 'INSOMNIA')
        

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)

