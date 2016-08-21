import string
import math
import itertools


def fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n-1, n) == 1
    
def int2base(x, base):
    digs = string.digits
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def findFactor(x):
    if fermat(x):
        return -1
    else:
        p = int(math.sqrt(x) + .5) + 1
        for i in itertools.count(2):
            if x%i == 0:
                return i
            if i > math.sqrt(x) + 1:
                break
            
        return -1

def main():
    N = 16
    J = 50
    num = ["1" for x in range(N)]
    printLines = []
    for attempt in xrange(2**(N-2)):
        #print attempt
        outputLine = ""
        prime = False
        s = bin(attempt)[2:].zfill(N-2)
        num[1:-1] = s
        currentnum = "".join(num)
        for b in range(2, 11):
            #print b
            converted = int(currentnum, b)
            #print "converted", converted
            factor = findFactor(converted)
            if factor != -1:
                outputLine += " " + str(factor) 
            else:
                prime = True
                break
            
        if not prime:
            print currentnum
            outputLine = str(currentnum) + outputLine + "\n"
            printLines.append(outputLine)

        if len(printLines) == J:
            return printLines


fout = open("c.out", "w")
fout.write("Case #1:" + "\n")
output = main()
for l in output:
    fout.write(l)
fout.close()
    
            
        
            
        
        
    
