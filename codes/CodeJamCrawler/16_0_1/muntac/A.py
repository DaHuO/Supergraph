if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        N = raw_input()
        N = int(N)
        if N == 0:
            print 'Case #%d: INSOMNIA' %(caseNr)
        else:
            all_seen = {}
            i = 1
            while len(all_seen) < 10:
                curr = N * i
                while curr > 0:
                    all_seen[curr % 10] = 1
                    curr /= 10
                i += 1        
            print 'Case #%d: %d' %(caseNr, N * (i - 1))

