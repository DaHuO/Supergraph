import re

def getCount(n):
    seen = dict()
    digits = dict()
    i = 0
    d = n
    while len(digits) < 10:
        i += 1
        d = n*i
        if d in seen:
            return -1
        
        seen[d] = 1
        
        while d > 0:
            cd = d%10
            digits[cd] = 1
            d //= 10
        
    return n*i

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = lines[0].strip()
curTest = 0
curLine = 1

def getLine():
    global curLine
    global lines
    curLine += 1
    return lines[curLine-1]

while curTest < int(numTests):    
    N = int(getLine())
    
    A = getCount(N)
    out = "INSOMNIA" if A is -1 else str(A)
    fw.write("Case #%d: %s\n" % (curTest+1, out))
    curTest += 1
                    
fr.close()
fw.close()