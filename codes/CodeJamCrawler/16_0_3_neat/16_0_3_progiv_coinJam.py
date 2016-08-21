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
        print ('Case #%d:' % (printcounter), file=ouf)

dels = ' '.join(map(str, range(3,12)))
dels = " "+dels
def solvetest():
        printstr(1)
        n,j = map(int, inf.readline().split())
        count = 0
        for i in range(j):
            num = [0]*n
            num[0] = num[-1] = 1
            pos = 1
            di = i
            while di>0:
                num[pos] = num[n-pos-1] = di % 2
                #~ print(di%2, di, 'a')
                di//=2
                pos+=2
            count += 1
            
            print(''.join(map(str, num))+dels, file = ouf)
#precount()
testnum = int(inf.readline())
for test in range(testnum):
        solvetest()
close_files()

