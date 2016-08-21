import os, time, sys
sys.setrecursionlimit(1800000)

case_start, case_end = 1, 100

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

n=-1
memo={}

def greedy(s):
    #print s
    size=len(s)
    if not size: return 0

    last=s[-1]
    if last=='+':
        return greedy(s[:-1])

    pre=''
    #print nums
    for i in range(size):
        cur=s[i]
        if cur=='-': pre+='+'
        else: pre+='-'

    return greedy(pre)+1

def solve( s ):
    #print s
    size=len(s)
    if s=='+'*size: return 0
    if s=='-'*size: return 1
    if s in memo: return memo[s]

    memo[s]=999999
    optimal=999999

    pre=''
    #print nums
    for i in range(size):
        cur=s[i]
        if cur=='-': pre+='+'
        else: pre+='-'

        now=pre+s[i+1:]
        cost=solve(now)
        optimal=min(optimal,cost)

    optimal+=1
    #print s, optimal
    memo[s]=optimal
    return optimal

'''
print solve( '------+++-' ) #map( int, "12 3 52 25 9 83 45 21 33 3".split() ) )
print len(memo)
sys.exit(0)
'''

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    line=lines[k].strip(); k+=1
    print line

    if case>=case_start and case<=case_end:
        memo.clear()
        #ans=solve(line)
        ans=greedy(line)
        log( 'Case #%d: %d' % (case,ans) )
    
    case+=1
    print

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
