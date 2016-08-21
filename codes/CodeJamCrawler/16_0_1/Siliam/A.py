if __name__ == "__main__":
    testcases = input()

    def get_digits(N, l):
        if N < 10:
            l.add(N)
            return l
        l.add(N%10)
        return get_digits(N/10, l)
        

    for caseNr in xrange(1, testcases+1):
        N = int(raw_input())
        if N == 0:
            print "Case #" + str(caseNr) + ": INSOMNIA"
            continue
            
        l = set()
        lastN = 0
        while len(l) < 10:
            lastN += N
            nl = get_digits(lastN, set() )
            for x in nl :
                l.add(x)
        
        print "Case #" + str(caseNr) + ": " + str(lastN)