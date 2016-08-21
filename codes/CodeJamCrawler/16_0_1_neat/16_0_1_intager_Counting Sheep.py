import os, time, sys

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

def solve( n ):
    if not n: return 'INSOMNIA'

    seen=set()
    k=n
    while len(seen)<10:
        seen.update( list(str(k)) )
        #print k,seen
        k+=n

    return str(k-n)

#print solve( map( int, "12 3 52 25 9 83 45 21 33 3".split() ) )
#print solve(1)
#sys.exit(0)


# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    n=int(lines[k]); k+=1

    if case>=case_start and case<=case_end:
        ans=solve( n )
        log( 'Case #%d: %s' % (case,ans) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
