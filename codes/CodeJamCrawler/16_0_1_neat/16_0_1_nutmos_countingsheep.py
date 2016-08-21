n = int(raw_input())

def printfunc(case,s):
    print "Case #" + str(case) + ": " + s

for i in range(1,n+1):
    m = int(raw_input())
    if m == 0:
        printfunc(i, "INSOMNIA")
    else:
        numlist = []
        k = 0
        while True:
            k += m
            for kk in str(k):
                if numlist.count(kk) == 0:
                    numlist.append(kk)
            if len(numlist) == 10:
                printfunc(i, str(k))
                break
