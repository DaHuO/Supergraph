from collections import Counter

def digits(N):
    if N==0:
        return [0]
    else:
        dd = []
        while N>0:
            dd.append(N%10)
            N = N//10
        return dd
    
f = open('large.txt','r')
fo = open('out.txt','w')

T = int(f.readline())
t = 1
for t in range(1,T+1):
    N = int(f.readline())
    
    
    if N==0:
        fo.write('Case #{:d}: INSOMNIA\n'.format(t))
        continue
    dset = set()
    M = 0
    while len(dset)<10:
        M += N
        for d in digits(M):
            if d not in dset:
                dset ^= {d}
                
    fo.write('Case #{:d}: {:d}\n'.format(t,M))
fo.close()
    
            
            
            

    
    
    
