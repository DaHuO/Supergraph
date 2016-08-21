import sys

def solve(N):
    
    if N == 0:
        return 'INSOMNIA'
    
    res = N; ctr = 1; 
    A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    B = [] 
    while A:
        s = map(int,str(res))
        B = list(set(B) | set(s))
        if not [a for a in A if a not in B]: 
            return res     
        ctr += 1
        res = ctr*N 
        
    return 0    
        

if __name__ == "__main__":
    f = open('A-large.in','r')
#    f = open('practice','r')
    T = int(f.readline().strip())
    ctr = 0 
    w = open('A-large.out','w')
    for i in xrange(T):
        ctr += 1
        N = map(int, f.readline().split(' '))
        res =  "Case #" + str(ctr) + ": " + str(solve(N[0]))
        print res
        w.write(res + '\n')

