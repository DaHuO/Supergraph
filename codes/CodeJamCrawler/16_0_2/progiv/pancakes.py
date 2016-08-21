import math
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
        pred = s[0]
        ans = 0
        #~ print(s, s[1:]+'+')
        for c in s[1:]+'+':
            if c!=pred:
                ans+=1
            pred = c
        printstr(str(ans))
#precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

