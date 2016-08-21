def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas):
    N, R, P, S = readvals()
    NN = P+R+S
    
    rules = {'PS':'S', 'PR':'P', 'RS':'R' }
    def check(orders):
        if len(orders)==1: return True
        nextord = ''
        for i in xrange(0, len(orders), 2):
            mat = ''.join( sorted(orders[i:i+2]) )
            if mat not in rules: return False
            nextord += rules[mat]
        return check(nextord)
    
    x, y, z = NN/2-R, NN/2-S, NN/2-P
    #~ print x,y,z
    if x<0 or y<0 or z<0 or x+y!=P or y+z!=R or x+z!=S: 
        print 'Case #%d: %s' % ( cas, 'IMPOSSIBLE' )
        return 
    allpairs = sorted(['PS']*x+['PR']*y+['RS']*z)
    checked = set()
    from itertools import permutations
    for p in permutations(allpairs):
        order = ''.join(p)
        if order not in checked: 
            if check(order): 
                print 'Case #%d: %s' % ( cas, order )
                return 
            checked.add(order)
    print 'Case #%d: %s' % ( cas, 'IMPOSSIBLE' )

def testcase(cas):
    
    def getxyz(p,r,s):
        nn = p+r+s
        x = nn/2-s # nb of PR
        y = nn/2-r
        z = nn/2-p
        return x,y,z
    
    N, R, P, S = readvals()
    for i in xrange(N):
        x,y,z = getxyz(P,R,S)
        if x<0 or y<0 or z<0 or x+y!=P or x+z!=R or y+z!=S: 
            print 'Case #%d: %s' % ( cas, 'IMPOSSIBLE' )
            return 
        P,S,R = x,y,z
    rules = {'S':'PS', 'P':'PR', 'R':'SR' }
    res = 'S'*S+'P'*P+'R'*R
    for i in xrange(N):
        newres = ''
        for c in res: newres += rules[c]
        res = newres
    #~ rules = {'S':'PS', 'P':'PR', 'R':'RS' }
    #~ newres = ''
    #~ for c in res: newres += rules[c]
    #~ res = newres
    for i in xrange(1,N+1):
        k = 2**i
        for j in xrange(0, len(res), k): 
            #~ if cas==16: print res[j:j+k/2], res[j+k/2: j+k],  res[j:j+k/2] > res[j+k/2: j+k]
            if res[j:j+k/2] > res[j+k/2: j+k]: 
                #~ print res
                tmp = res[j+k/2:j+k]+res[j:j+k/2]
                res = res[:j]+tmp+res[j+k:]
                #~ print res
    
    print 'Case #%d: %s' % ( cas, res )
    


if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)
