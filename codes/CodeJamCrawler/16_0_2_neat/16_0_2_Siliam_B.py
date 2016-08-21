if __name__ == "__main__":
    testcases = input()

    def count_inflections(s):
        state = s[:1]
        i = 0
        for c in s[1:] :
            if c != state :
                i += 1
                state = c
        return i
        

    for caseNr in xrange(1, testcases+1):
        s = raw_input()
        k = count_inflections(s)
        if s[-1] == '-' :
            k += 1
        
        print "Case #" + str(caseNr) + ": " + str(k)