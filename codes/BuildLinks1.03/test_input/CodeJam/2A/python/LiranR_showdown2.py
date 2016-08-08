import itertools as it
   
exp = dict( [ ("R","RS") , ("P", "PR"), ("S", "SP") ] )

def swap(s, pos1, pos2, length):
    '''
    swap the two substrings of s of the given length in the given positions
    assume that pos1 + length <= pos2
    '''
    return s[:pos1] + s[pos2:pos2+length] + s[pos1+length:pos2] + \
           s[pos1:pos1+length] + s[pos2+length:]
    
def multisort(s, n):
    '''
    given a tournament s, return the lexicographically first equivalent
    '''
    for i in xrange(1,n+1):
        for j in xrange(0,len(s),2**i):
            if s[j:j+2**(i-1)] > s[j+2**(i-1):j+2**i]:
                s = swap(s, j, j+2**(i-1), 2**(i-1) )
    return s

def winners(n):
    ans = []
    for c in ["R","P","S"]:
        cur = c
        for i in xrange(n):
            cur = "".join( exp[x] for  x in cur )
        ans.append(multisort(cur,n))
    return ans

def sol_quick(N,R,P,S):
    for w in winners(N):
        if w.count("R") == R and w.count("P") == P and w.count("S") == S:
            return w
    return "IMPOSSIBLE"
    
        
T = int(raw_input())
for t in xrange(1,T+1):
    N,R,P,S = map(int, raw_input().split())
    print "Case #%d: %s"%(t, sol_quick(N,R,P,S))
