__author__ = 'Arwin'
import numpy as np

fn = 'A-large.in'
f = open(fn)
ansf = open("ans.txt", "w")

def getd(S):
    numbers= ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    p= [[0]*26 for i in range(10)]
    for i,n in enumerate(numbers):
        for c in n:
            p[i][ord(c)-ord('A')]+=1
    countl=[0]*26
    for c in S:
        countl[ord(c)-ord('A')]+=1
    ans= np.array(countl)
    x = np.rint(np.linalg.lstsq(np.transpose(np.array(p)), ans)[0]).astype(int)
    tel=''
    for i,xx in enumerate(x):
        for cc in range(xx):
            tel+=str(i)
    return tel

T= int(f.next())
for i in xrange(1,T+1):
    S= f.next().strip()
    ansf.write( 'Case #{0}: {1}\n'.format(i, getd(S) ) )

ansf.close()