def set(mask, N):
    while N > 0:
        bit = N % 10
        mask |= (1 << bit)    
        N /= 10        
    return mask
    
def solve(case):
    N = int(raw_input())
    mask = 0
    i = 1
    ans = "Case #%s: %s"
    explored = dict()
    k = 1000000
    while k > 0:        
        k -= 1
        M = N*i
        if M in explored:
            return ans % (str(case), "INSOMNIA")                
        explored[M] = True
        mask = set(mask, M)                
        if mask == 1023:
            return ans % (str(case), str(M))
        i += 1                        
        
T = int(raw_input())
for case in xrange(T):
    print solve(case+1)


