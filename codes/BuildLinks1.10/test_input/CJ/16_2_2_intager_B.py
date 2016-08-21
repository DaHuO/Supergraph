import os, time, sys, string

case_start, case_end = 1, 200

cur_dir=os.path.dirname( os.path.abspath(__file__) )
output=None

def log( msg ):
    print msg
    output.write( msg + '\n' )

lines=[]
for f in os.listdir( cur_dir ):
    if f.lower().endswith( '.in' ):
        if not 'output' in f:
            lines=open( os.path.join( cur_dir, f ), 'r' ).readlines()
            outpath=f.split( '.' )[0] + '_output_%d_%d.txt' % (case_start, case_end)
            print f, '-->', outpath
            output=open( os.path.join( cur_dir, outpath ), 'w' )
            break

start = time.time()

# ------------------------------------------------------- 

C='1?'
J='2?'
n=len(C)
power=[]

best=0
besta,bestb='',''

def recurse( i, a,b, diff ):
    global best, besta, bestb

    if i:
        if abs(diff)-power[i-1] > best:
            #print 'PRUNE', a,b,'-->',diff, abs(diff)-power[i-1], best
            return

    if i==n:
        #print a,b,'-->',diff
        diff=abs(diff)
        if diff<best:
            best=diff
            besta, bestb=a,b
        return

    avals=C[i]
    if avals=='?':
        avals=string.digits

    bvals=J[i]
    if bvals=='?':
        bvals=string.digits

    for aval in avals:
        for bval in bvals:
            localdiff=power[i]*( int(aval)-int(bval) )
            recurse(i+1,a+aval,b+bval,diff+localdiff)

def solve():
    global power, best, besta, bestb, n

    n=len(C)
    exp=10**(n-1)
    best=10*exp

    power=[]
    for i in range(n):
        power.append(exp)
        exp/=10

    recurse( 0, '', '', 0 )
    #print nums

    return best, besta, bestb

'''
test=map( int, "1 2 3".split() )
print solve( )
sys.exit(0)
'''

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    C,J=lines[k].split(); k+=1

    if case>=case_start and case<=case_end:
        solve()
        log( 'Case #%d: %s %s' % (case,besta, bestb) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
