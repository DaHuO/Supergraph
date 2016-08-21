import sys
#cat countsheep | python CountingSheep.py
def startme():
    testcases = int(sys.stdin.readline())
    outfile = file("./A-large.res", "w")
    digits = range(0,10)
    for tc in range(0, testcases):
        res = None
        saveddigits=[]
        saveddigitsrecs=[]
        nval = int(sys.stdin.readline())
        bbreak = False
        icount = 1
        while icount <= 200:
            for digit in digits:
                if str(digit) in str(icount*nval) and digit not in saveddigits:
                    saveddigits.append(digit)
                    saveddigitsrecs.append(icount*nval)
                    saveddigits.sort()
                    if digits == saveddigits:
                        bbreak = True
                        res = icount*nval
            if bbreak:
                break
            icount += 1
        if res!=None:
            outfile.write("Case #%s: %s\n" % (str(tc+1), res))
        else:
            outfile.write("Case #%s: INSOMNIA\n" % (str(tc+1)))
    outfile.close()
startme()