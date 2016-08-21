#!/usr/bin/env python

def printResult(case, result):
    print "Case #{}: {}".format(case, str(result))

def remove(s1, s2):
    for c in s2:
        i = s1.index(c)
        s1 = s1[:i] + s1[(i+1):]
    return s1

if __name__ == "__main__":    
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s, = [str(s) for s in raw_input().split(" ")]
        pnum = []
        while 'X' in s:
            s = remove(s, 'SIX')
            pnum.append('6')
        while 'Z' in s:
            s = remove(s, 'ZERO')
            pnum.append('0')
        while 'W' in s:
            s = remove(s, 'TWO')
            pnum.append('2')
        while 'G' in s:
            s = remove(s, 'EIGHT')
            pnum.append('8')
        while 'U' in s:
            s = remove(s, 'FOUR')
            pnum.append('4')
        while 'F' in s:
            s = remove(s, 'FIVE')
            pnum.append('5')
        while 'V' in s:
            s = remove(s, 'SEVEN')
            pnum.append('7')
        while 'O' in s:
            s = remove(s, 'ONE')
            pnum.append('1')
        while 'T' in s:
            s = remove(s, 'THREE')
            pnum.append('3')
        while 'N' in s:
            s = remove(s, 'NINE')
            pnum.append('9')
        pnum.sort()
        result = ''
        for x in pnum:
            result += x
        printResult(i, result)
