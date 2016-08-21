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

letts=[ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]

LIM=20
lett2num={}

def strSort( s ):
    l = [c for c in s]
    l.sort()

    # Join the characters together.
    result = "".join(l)
    return result

def recurse( lett, num, start ):
    global lett2num

    if len(lett) > LIM: return

    lett=strSort(lett)

    #print repr(lett), repr(num), '<<-- REP'
    #print lett, '-->', num
    lett2num[lett]=num

    for i in range(start,10):
        recurse( lett+letts[i], num+str(i), i )

def solve( lett ):
    #print 'solve', strSort(lett), lett2num[strSort(lett)]
    return lett2num[strSort(lett)]

recurse( '', '', 0 )
print len(lett2num)

'''
print solve( 'OZONETOWER' )
print solve( 'OURNEONFOE' )
sys.exit(0)
'''

# ------------------------ main ------------------------------- 
k=1
case=1

while k<len(lines):
    s=lines[k].strip(); k+=1

    if case>=case_start and case<=case_end:
        ans=solve(s)
        log( 'Case #%d: %s' % (case,ans) )
    
    case+=1

elapsed = time.time() - start
print 'elapsed', elapsed

'''

'''
