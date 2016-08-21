
def solve(inval):
    # print "Init", inval
    pancakes = inval[::-1]
    count = 0
    for i in xrange(0, len(pancakes)):

        if pancakes[i]=="-":
            count = count + 1
            # flip from i to the rest
            j=i

            while (j<len(pancakes)):
                flip = "+" if pancakes[j]=="-" else "-"
                pancakes = pancakes[:j] + flip + pancakes[j+1:]
                j=j+1
        # print "".join(reversed(pancakes))

    return count
if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        inval = raw_input()
        print("Case #%i: %s" % (caseNr, solve(inval)))
