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
        n = int(inf.readline())
        #~ print(n)
        if n == 0:
            printstr('INSOMNIA')
        else:
            i = 1
            s = set(map(int,str(n)))
            while (full != s) and i<100:
                #~ print(i,n,s, full in s)
                i+=1
                for c in map(int, str(i*n)):
                    s.add(c)
            printstr(i*n)
#precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

