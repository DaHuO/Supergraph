import os, time, sys

case_start, case_end = 1, 50

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

'''
In sample case #4, the largest possible circle seats the following kids in the following order: 
7 9 3 10 4 1

1 7
2 8
3 10
4 10
5 9
6 2
7 9
8 6
9 3
10 3
'''

best=0

LIM=11

free=[True]*LIM

kids=[7, 8, 10, 10, 9, 2, 9, 6, 3, 3]
bff=[0]*LIM
INC=range(1,len(kids)+1)

first=0
circle=[0]*LIM

from itertools import permutations

def check( p ):
    opt=1
    L=len(p)

    i=1
    while i<L-1:
        mid=p[i]
        if bff[mid]!=p[i-1] and bff[mid]!=p[i+1]: break
        i+=1
    
    for j in range(1,i+1):
        if bff[ p[0] ]==p[1] or bff[ p[0] ]==p[j]:
            if bff[ p[j] ]==p[0] or bff[ p[j] ]==p[j-1]:
                opt=max(opt,j)

    return opt

'''
def check( p ):
    opt=1
    for i in range(2,n+1):
        opt=max(opt,check2( p[:i] ))
    return opt
'''

def solve( level, prev1, prev2 ):
    global best, free, circle

    #print level, prev1, prev2

    '''
    print 'level=', level, '\t',
    for i in range(level-1):
        print circle[i+1],
    print
    '''

    if bff[prev2]==first: # bff[first]==prev2 or 
        #best=max(best,level-1)

        if level>best:
            best=level

            '''
            print '\t\t best=', best
            for i in range(level-1):
                print circle[i+1],
            print
            '''
        #print 'best=', best

    if bff[prev2]==prev1:
        best=max(best,level)
        #print nums
        for k in INC:
            if free[k]:
                if bff[k]==prev2:
                    free[k]=False
                    circle[level]=k
                    solve(level+1,prev2,k)
                    free[k]=True

    else:
        k=bff[prev2]
        if free[k]:
            free[k]=False
            circle[level]=k
            solve( level+1, prev2, k )
            free[k]=True



def answer(kids):
    global bff, first, best, n

    best=1
    n=len(kids)

    for i,k in enumerate(kids):
        print i+1,k
        bff[i+1]=k

    for p in permutations( range(1,n+1) ):
        loc=check(p)
        if loc>best:
            print p, check(p)
            best=loc
        #best=max(best, check(p))

    return best+1

    '''
    for i in INC:
        for j in INC:
            if bff[i]==j:
                first=i
                circle[1]=i; circle[2]=j
                free[i]=False
                free[j]=False
                solve(3,i,j)
                free[i]=True
                free[j]=True

    return best-1
    '''

#print answer(kids)
#print solve( map( int, "12 3 52 25 9 83 45 21 33 3".split() ) )
#sys.exit(0)

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    n=int(lines[k]); k+=1
    kids=map( int, lines[k].split() ); k+=1

    if case>=case_start and case<=case_end:
        ans=answer(kids)
        log( 'Case #%d: %d' % (case,ans) )
        print
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
