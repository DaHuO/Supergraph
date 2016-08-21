##def solve(S):
##    r = ""
##    for s in S:
##        if len(r) == 0:
##            r+=s
##        else:
##            if r[0]<=s:
##                r= s + r
##            else:
##                r+=s
##    return r

##print solve("CAB")
##print solve("JAM")
##print solve("CODE")
##print solve("ABAAB")
##print solve("CABCBBABC")
##print solve("ABCABCABC")
##print solve("ZXCASDQWE")

def solveB(data, size):
    c = {}
    for i in xrange(len(data)):
            if data[i] not in c:
                c[data[i]] = 1
            else:
                c[data[i]]+=1
    r = []
    for e in c:
        if c[e]%2 != 0:
            r.append(e)
    r.sort()
    return r

##data = [[1,2,3],[2,3,5],[3,5,6],[2,3,4],[1,2,3]]
##print solveB(data,3)

        
            
        
    

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases + 1):
        size = input()
        data = []
        for i in xrange(2* size -1):
            line = raw_input()
            l = [int(_) for _ in line.split()]
            data.extend(l)
        res = solveB(data, size)
        s_res = " ".join([str(e) for e in res])
        print("Case #%i: %s" % (caseNr, s_res))
        #print("Case #1:")
