import sys

def getNumberOfInversions(inList):
    prev, cur = None, None
    
    numOfInversions = 0
    inList += '+'
    # print("Extended inList = {0}".format(inList))
    for c in inList:        
        cur = c
        # print("Current, Previous = {0}, {1}".format(cur, prev))
        if prev is None:
            prev = cur
            continue
        
        if cur != prev:
            numOfInversions = numOfInversions + 1
            prev = cur
    
    return numOfInversions

def main():
    ln = 0
    T = None
    for line in sys.stdin:
        if ln == 0:
            T = int(line)
            ln += 1
        else:
            inStr = line.rstrip()
            sol = getNumberOfInversions(inStr)
            print("Case #{0}: {1}".format(ln, sol))
            ln += 1

if __name__ == '__main__':
    main()
