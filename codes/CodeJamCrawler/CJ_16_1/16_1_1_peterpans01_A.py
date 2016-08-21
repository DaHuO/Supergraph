def solve(S):
    r = ""
    for s in S:
        if len(r) == 0:
            r+=s
        else:
            if r[0]<=s:
                r= s + r
            else:
                r+=s
    return r

##print solve("CAB")
##print solve("JAM")
##print solve("CODE")
##print solve("ABAAB")
##print solve("CABCBBABC")
##print solve("ABCABCABC")
##print solve("ZXCASDQWE")

if __name__ == "__main__":
    testcases = input()
         
    for caseNr in xrange(1, testcases + 1):
        T = raw_input()
        res = solve(T)
        print("Case #%i: %s" % (caseNr, res))
        #print("Case #1:")
