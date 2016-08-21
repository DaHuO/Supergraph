#codejam 4/8/2016
import math #as m
import time
#import codejam
import sys
import os
import random
sys.setrecursionlimit(205) #sometimes we need 1000 max

cwd = os.getcwd()
filename = cwd+r'\a-test.in.txt'
filename = cwd+r'\a-small-attempt0.in'
filename = cwd+r'\a-large.in'
#filename = cwd+r'\a-small-practice.in'
foutname = filename.replace(".in",".out")

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def ceildiv(x, d):#like x//d but ceiling, for positives only
    return (x + (d-1)) // d

def baseN(num,b):
    """Return num as a string in base b"""
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

#print baseN(16,2),"=10000 ?"
#print baseN(28,3),"=1001 ?"




def sol1(S,dbg=1):#S=list of letters
    #return tuple of answer as string, path

    ret = []
    for ch in S:
        if len(ret)==0:
            ret.append(ch)
        elif ch>=ret[0]:
            ret.insert(0,ch)
        else:
            ret.append(ch)
    return (''.join(ret),None)

        
dbg=0
if dbg: print "T=",T
if 1:
  t0 = time.time()
  sumz = 0
  for iit in range(1,T+1):
    rawline = FILE.readline()
    if rawline is None or rawline=='' or rawline=='\n':
        print "EOF reached before T=",T," - quit early. i=",iit
        break
    rawline = rawline.rstrip().split(' ') #no newline at end

    #print len(rawline),str(rawline)
    nparams=1
    #N,J = [int(a) for a in rawline[:nparams]]
    S = rawline[0]
    if len(rawline)>nparams: manual_ans = rawline[nparams] #manually computed answer as string
    else: manual_ans = None
    
    if dbg: print "Attempt Case #" + str(iit)+": S,manual_ans=",S,manual_ans

    codepath = None
    results = sol1(S,dbg)
    if len(results)<=1: raise Exception("sol1 didn't give len desired! "+str(len(results)))
    msg = 'Case #' + str(iit) + ': '+results[0]
    if dbg: print msg
    if not dbg and iit%10==1: print msg
    FOUT.write(msg + "\n")
    if dbg: print ""
  print "finished",T,"cases,", round(time.time() - t0,3),"s, sumz:",sumz
FOUT.close()
FILE.close()

    
