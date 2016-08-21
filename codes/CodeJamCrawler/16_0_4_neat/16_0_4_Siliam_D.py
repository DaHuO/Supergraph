if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        K, C, S = map(int, raw_input().split())
        if S == K:
            positions = xrange(1, K+1)
            
        print "Case #" + str(caseNr) + ": " + " ".join(map(str, positions))