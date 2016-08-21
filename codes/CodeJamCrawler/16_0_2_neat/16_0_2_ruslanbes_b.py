import math, sys


quaternion = {
    "i": {"j": (True, "k"), "k": (False, "j") },
    "j": {"i": (False, "k"), "k": (True, "i") },
    "k": {"i": (True, "j"), "j": (False, "i") },
}

def q( a, b ):
    if a == (True, "1"):
        return b
    elif a == (False, "1"):
        return not b[0], b[1]
    elif b == (True, "1"):
        return a    
    elif b == (False, "1"):
        return not a[0], a[1]

    sign = (a[0] == b[0])
    if a[1] == b[1]:
        return ( not sign , "1")
    if sign:
        return quaternion[ a[1] ] [ b[1] ]
    else: 
        return quaternion[ b[1] ] [ a[1] ]

def q_str(str, sign = True):
    tmp = (sign, "1")
    for x in str:
        tmp = q(tmp, (True, x))
    return tmp

def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "impossible"
    outputLine = casestr+status
    print outputLine

def main():


    ############################################1
    T = int( raw_input() )
    for t in xrange(T):    
        line = raw_input()
        flips = 0
        pos = "+"
        neg = "-"
        line = line.rstrip(pos)
        while len(line) > 0:
            if line[0] == neg:
                flips += 1
                line = line[::-1]
                pos, neg = neg, pos
                line = line.rstrip(pos)
            else:
                line = line.lstrip(pos)
                line = line.lstrip(neg)
                flips += 2
                line = line[::-1]
                pos, neg = neg, pos
                line = line.rstrip(pos)
        output(t, flips)

if __name__ == "__main__":
   main()