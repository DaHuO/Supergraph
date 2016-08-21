
def solve(inval):
    # print "input", inval
    N = int(inval)
    visited = dict()
    i=1
    threshold = 10000
    while True:
        prevLen = len(visited.keys())
        for c in str(N*i):
            if visited.has_key(c)==False:
                visited[c] = True
        newLen = len(visited.keys())
        # print visited
        if newLen==10:
            return N*i # done
        if prevLen!=newLen:#changed?
            unchanged = 0
        else:
            unchanged = unchanged + 1
        if unchanged>threshold:
            return "INSOMNIA"
        i += 1

    return str(fcnt)
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        inval = raw_input()
        print("Case #%i: %s" % (caseNr, solve(inval)))
