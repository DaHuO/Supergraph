        

def testcase(ind): # pincakes
    global S, opt_nb # python's var scoping... @@
    S = raw_input()
    l = len(S)
    final_state = '+'*l
    max_n = 2*l # upper bound for optimal solution
    opt_nb = max_n
    
    def flip(s, i): #flip pincakes [0,1,...,i]
        res = ''
        for j in xrange(i, -1, -1):
            res += '+' if s[j]=='-' else '-'
        return res + s[i+1:] 
    
    def lower_bound(s):
        cnt = 0 
        for i in xrange(l-1):
            if s[i]!=s[i+1]: 
                cnt += 1
                if i>=1 and s[i-1]==s[i+1]: cnt -= 1
        return cnt
    
    # method 1: dfs searching + branch cutting --> too slow...
    def search(step): # dfs searching for solution
        global S, opt_nb
        if step+lower_bound(S) > opt_nb: # cutting branch here
            return 
        if S==final_state:
            opt_nb = min(opt_nb, step)
            return 
        for i in xrange(l):
            S = flip(S,i)
            search(step+1) # dfs
            S = flip(S,i) # backtracking
    #~ search(0)
    
    # method 2: dp
    dp = {} # mapping a str (pincake state) to the nb of min ops
    def pincake_rec(s):
        if s in dp: return dp[s]
        if s==final_state: 
            dp[s] = 0
            return dp[s]
        dp[s] = -1 # to avoid infinite rec-call...
        res = max_n
        for i in xrange(l):
            s2 = flip(s,i)
            nb = pincake_rec(s2)
            if nb==-1: continue
            res = min(nb+1, res)
        for i in xrange(l): # setting the -1 above might cause bug !!...
            s2 = flip(s,i)
            dp[s2] = min(dp[s2], res+1)
        dp[s] = res
        return res
    #~ opt_nb = pincake_rec(S)
    #~ print 'Case #%d: %d' % (ind, opt_nb)
    
    # method 3: BFS?
    
    def turning_pts(s):
        res = set([l-1]) # the last pincake is always a turning point
        for i in xrange(l-1):
            if (i>0 and s[i]!=s[i-1]) or (s[i]!=s[i+1]):
                res.add(i)
        return res
    
    def compress(s):
        res = ''
        last_c = '*'
        for c in s:
            if last_c != c: 
                res += c
                last_c = c
        return res
    
    layer = [S]
    visited = set()
    depth = 0
    while len(layer)!=0:
        new_layer = set()
        for s in layer: 
            s = compress(s)
            visited.add(s)
            if s=='+': 
                opt_nb = depth
                print 'Case #%d: %d' % (ind, opt_nb)
                return 
            for i in xrange(len(s)):
                s2 = flip(s,i)
                s2 = compress(s2)
                #~ if lower_bound(s2)>lower_bound(s): continue
                if s2 not in visited: 
                    new_layer.add( s2 )
        depth += 1
        layer = new_layer
    
        

import sys
sys.setrecursionlimit(10000) # we need 2**10 recursive calls for small case...

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(T):
        testcase(i+1)

