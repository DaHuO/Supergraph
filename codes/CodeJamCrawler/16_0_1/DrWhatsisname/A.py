import sys

def getDigits(n):
    ds = set()
    while n > 0:
        ds.add(n%10)
        n/=10
    return ds


with open(sys.argv[1]) as inFile:
    with open(sys.argv[1]+".out", 'w') as outFile:
        ntests = int(inFile.readline())
        for t in range(1, ntests+1):
            n = int(inFile.readline()) 
            if n == 0:
                outFile.write("Case #" + str(t) + ": INSOMNIA\n")
                continue
            m = n
            ds = set()
            while ds != {0,1,2,3,4,5,6,7,8,9}:
                ds = ds.union(getDigits(m))
                m += n 
            outFile.write("Case #" + str(t) + ": " +str(m-n) + "\n")
