import os, time, sys, math

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

from baseconv import BaseConverter

convs=[None,None]
for i in range(2,11):
    s="".join( str(j) for j in range(i) )
    print s
    convs.append( BaseConverter(s) )

def jams(n):
    vals=[]
    for i in range(2,11):
        vals.append( int(convs[i].decode(n)) )
    return vals

def is_prime(num):
    for j in range(2,int(math.sqrt(num)+1)):
        if (num % j) == 0:
            return j
    return 0

def check(n):
    divs=[]
    for j in jams(n):
        p=is_prime(j)
        if not p: return None
        divs.append(p)
    return divs
    #return (divs,jams(n))

#base2 = BaseConverter('01')
#print base2.decode(1001)
#print check(1001)

n=-1
found=0

def solve( N ):
    global found

    bits=N-2
    for bit in range(2**bits):
        n=int( '1'+convs[2].encode(str(bit)).zfill(bits)+'1' )
        ch=check(n)
        if ch:
            print n, " ".join( str(k) for k in ch )

            found+=1
            if found==50: break

    print found
    #return ans

#print solve( map( int, "12 3 52 25 9 83 45 21 33 3".split() ) )
solve(16)
sys.exit(0)

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    n=int(lines[k]); k+=1
    points=[]
    for i in range(n):
        points.append( map( int, lines[k].split() )); k+=1

    if case>=case_start and case<=case_end:
        ans=solve( points )
        log( 'Case #%d: %d' % (case,ans) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
