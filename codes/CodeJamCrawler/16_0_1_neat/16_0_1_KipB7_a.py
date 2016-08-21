#codejam 5/10/2015
import math as m
import time
#import codejam
import sys
import os
sys.setrecursionlimit(100) #sometimes we need 1000 max

cwd = os.getcwd()
filename = cwd+r'\a-test.in.txt'
#filename = cwd+r'\A-small-attempt0.in'
filename = cwd+r'\big.in'
filename = cwd+r'\A-large.in'
#filename = cwd+r'\a-small-practice.in'
foutname = filename.replace(".in",".out")

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def ceildiv(x, d):#like x//d but ceiling, for positives only
    return (x + (d-1)) // d

def sol1(N, dbg):
    seen=[0]*10 #one for each digit
    lastnum = N
    path = []
    for m in xrange(1000):
        #path.append(lastnum)
        for ch in str(lastnum):
            seen[ord(ch)-ord('0')]=1
        if sum(seen)==10:
                return lastnum,[m]#path
        lastnum += N
    return "INSOMNIA",["All"]
    #answer and path to answer

dbg=0
if dbg: print "T=",T
if 1:
  t0 = time.time()
  sumz = 0
  for i in range(1,T+1):
    rawline = FILE.readline()
    if rawline is None or rawline=='':
        print "EOF reached before T=",T," - quit early. i=",i
        break
    rawline = rawline.split(' ')
    nparams=1
    if len(rawline)>nparams: rawline[-1]=rawline[-1].rstrip() #manual answer
    #N = [int(a) for a in rawline[:nparams]]
    N = int(rawline[0])
    if len(rawline)>nparams: manual_ans = [int(rawline[nparams]) if rawline[nparams].isdigit() else rawline[nparams] ]#manually computed answer
    else: manual_ans = None
    
    if dbg: print "Case #" + str(i)+": N,ans=",N,manual_ans

    z1,codepath = sol1(N, dbg)

    #if dbg: print "  ==> ",z1
    sumz += z1 if isinstance(z1,(int,long)) else 0
    msg = 'Case #' + str(i) + ': ' + str(z1)
    if dbg:
        if manual_ans: print msg+ (" 1 is OK!" if manual_ans[0]==z1 else "1 DIFF!") + " Path="+str(codepath)
        else: print msg + " Path="+str(codepath)
    if not dbg and i%10==1: print msg
    FOUT.write(msg + "\n")
    if manual_ans!=None:
        if manual_ans[0]!=z1: print "...DIFFERENT! ",manual_ans," but we got: ",(z1),"  Case #" + str(i)
    if dbg: print ""
  print "finished",T,"cases,", round(time.time() - t0,3),"s, sumz:",sumz
FOUT.close()
FILE.close()
