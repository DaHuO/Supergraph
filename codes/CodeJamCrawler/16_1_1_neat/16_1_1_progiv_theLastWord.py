import math
import sys
sys.setrecursionlimit(1000000)
inf = open("in.in", "r")
ouf = open('out.out','w')

def close_files():
        inf.close()
        ouf.close()

def precount():
        pass

printcounter = 0
def printstr(a):
        global printcounter
        printcounter +=1
        print ('Case #%d: %s' % (printcounter,a), file=ouf)

full = set(range(10))
def solvetest():
        s = inf.readline().strip()
        n = len(s)
        a = ['a']*n
        l=0
        r=n-1
        last=n
        pred = n
        while r>=l:
            curmaxi=0
            curcount=0
            for i in range(last):
                if s[curmaxi]<s[i]:
                    curmaxi = i
                    curcount = 1
                elif s[curmaxi]==s[i]:
                    pred = curmaxi
                    curmaxi = i
                    curcount +=1
            last-=1
            while last>curmaxi:
                a[r] = s[last]
                r-=1
                last-=1
            a[l] = s[curmaxi]
            l+=1
        printstr(''.join(a))
#precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

