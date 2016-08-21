#codejam 4/8/2016
import math as m
import time
#import codejam
import sys
import os
sys.setrecursionlimit(205) #sometimes we need 1000 max

cwd = os.getcwd()
filename = cwd+r'\b-test.in.txt'
filename = cwd+r'\b-small-attempt0.in'
filename = cwd+r'\B-large.in'
#filename = cwd+r'\b-small-practice.in'
foutname = filename.replace(".in",".out")

FILE = open(filename)
FOUT = open(foutname,"w")
T = int(FILE.readline())

def ceildiv(x, d):#like x//d but ceiling, for positives only
    return (x + (d-1)) // d

def sol1(S, dbg): #S is string of + and -
    bin = [1 if ch=='+' else 0 for ch in S] # + = 1 = happy side up, - = 0
    #if sum(bin)==len(bin): return 0,["perfect"]
    #if sum(bin)==0: return 1,[1]

    #find last 0 - we flip this and what is on its left, leaving rest alone

    ans, depth = sol1b(bin,1,0,dbg=0)
    return ans, [depth]
    #answer and path to answer

def sol1b(bin, goal, depth, dbg):
    """bin is array of 1 and 0; goal is 0 or 1; dbg can be true.
    Returns number of flips to achieve goal and depth required. """
    if len(bin)==0: raise "empty!?!"
    if dbg: print "sol1b("+str(bin)+", goal="+str(goal)+", depth="+str(depth)
    sumbin = sum(bin)
    if sumbin==len(bin)*goal: return 0,depth #no flips, already perfect
    if sumbin==len(bin)*(1-goal): return 1,depth #all reversed, flip stack

    #find last one that is not goal
    for rk,b in enumerate(bin[::-1]): #reverse order
        if b==goal: continue #keep looking back
        #found non-goal - needs flipping
        k = len(bin)-1-rk #forward counting position of found non-goal
        #k and to left will need to be flipped
        if dbg: print "found ",b,"<>goal of",goal,", recurse on k=",k,"bin=",bin
        ans, depth2 = sol1b(bin[:k+1],1-goal,depth+1,dbg) 
        return 1+ans,depth2
    raise "never gets here, we tested sumbin "+str(sumbin)+" above! bin="+str(bin[:100])
        
dbg=0
if dbg: print "T=",T
if 1:
  t0 = time.time()
  sumz = 0
  for i in range(1,T+1):
    rawline = FILE.readline()
    if rawline is None or rawline=='' or rawline=='\n':
        print "EOF reached before T=",T," - quit early. i=",i
        break
    rawline = rawline.rstrip().split(' ') #no newline at end
    nparams=1
    #N = [int(a) for a in rawline[:nparams]]
    S = rawline[0] #string of +-'s
    #print "testing!!! 10x"
    #S = S * 10
    if len(rawline)>nparams: manual_ans = rawline[nparams] #manually computed answer as string
    else: manual_ans = None
    
    if dbg: print "Attempt Case #" + str(i)+": S,manual_ans=",S,manual_ans

    z1,codepath = sol1(S, dbg)
    z1str = str(z1)
    
    #if dbg: print "  ==> ",z1str
    sumz += z1 if isinstance(z1,(int,long)) else 0
    msg = 'Case #' + str(i) + ': ' + z1str
    if dbg:
        if manual_ans: print msg+ (" is OK!" if manual_ans==z1str else " is DIFF!") + " Path="+str(codepath)
        else: print msg + " Path="+str(codepath)
    if not dbg and i%10==1: print msg
    FOUT.write(msg + "\n")
    if manual_ans != None:
        if manual_ans != z1str:
            print "...DIFFERENT! ",manual_ans," but we got: ",z1str,"  Case #" + str(i)
    if dbg: print ""
  print "finished",T,"cases,", round(time.time() - t0,3),"s, sumz:",sumz
FOUT.close()
FILE.close()
