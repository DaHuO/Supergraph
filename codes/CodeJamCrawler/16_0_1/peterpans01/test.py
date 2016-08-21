def test(N):
    if N == 0:
        return -1
    result = [_ for _ in xrange(10)]
    for i in xrange(1, 10001):
        k = N * i
        m = str(k)
        for s in m:
            temp = int(s)
            if temp in result:
                result.remove(int(s))
        if len(result) == 0:
            return k
    return -1

# print test(1)
# print test(5)
# print test(15)
# print test(19)
                    
if __name__ == "__main__":
    testcases = input()
       
    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        k = test(int(cipher))
        r = ""
        if k < 0:
            r = "INSOMNIA"
        else:
            r = str(k)
             
        print("Case #%i: %s" % (caseNr, r))
