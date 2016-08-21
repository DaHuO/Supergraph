import sys

def solve(N):
    B = [ord(b) for b in N]    
    swapd = 0; res = 0 
    for b in reversed(B):
        if b+swapd == 45: 
            if swapd == 2: 
                swapd = 0 
            else :
                swapd = 2 
            res += 1 
            
    return res
        

if __name__ == "__main__":
    f = open('B-large.in','r')
#    f = open('practice','r')
    T = int(f.readline().strip())
    ctr = 0 
    w = open('B-large.out','w')
    for i in xrange(T):
        ctr += 1
        N = f.readline()
        res =  "Case #" + str(ctr) + ": " + str(solve(N))
        print res
        w.write(res + '\n')

