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
#filename = cwd+r'\a-small-attempt0.in'
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


def flet(ch): return ord(ch)-ord('A')

LETST = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'
LETSA = LETST.split(' ');
NUMLET = [len(L) for L in LETSA]

def sol1(S,dbg=1):#S=list of letters
    #return phone number and path

    ret = []
    letct = [0]*26
    for ch in S:
        ich = ord(ch)-ord('A')
        letct[ich] += 1
    numdig = [0]*10
    numdig[8] = letct[flet('G')]
    numdig[3] = letct[flet('H')] - numdig[8]
    numdig[0] = letct[flet('Z')]
    numdig[4] = letct[flet('U')]
    numdig[6] = letct[flet('X')]
    numdig[2] = letct[flet('W')]
    numdig[1] = letct[flet('O')] - numdig[0] - numdig[2] - numdig[4]
    numdig[5] = letct[flet('F')] - numdig[4]
    numdig[7] = letct[flet('V')] - numdig[5]
    numdig[9] = (letct[flet('N')] - numdig[1] - numdig[7])//2
    #if dbg: print S,numdig
    ret=[]
    chklen = 0
    chklets = []
    for inum in range(10):
        if numdig[inum]>0: ret.append(`inum` * numdig[inum])
        chklen += numdig[inum] * NUMLET[inum]
        chklets.append(LETSA[inum] * numdig[inum])
    if chklen <> len(S): raise Exception('mismatch!! %d<>%d S=%s %s'%(chklen,len(S),S,`numdig`))

    #check all
    S_Sorted = sorted(S)
    CHK_Sorted = sorted(''.join(chklets))
    if ''.join(S_Sorted) != ''.join(CHK_Sorted): raise Exception('letters mismatch!')
    
    return (''.join(ret),None)

def tst():
    a='ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE'
    b=a.split(' ')
    ct = [0]*26
    for ch in a:
        if ch==' ': continue
        ct[flet(ch)] += 1
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        print ch +'='+`ct[flet(ch)]`,
    print ' '

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

    
