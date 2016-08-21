# import numpy as np

if __name__ == '__main__':
    
    fin = open('D-large.in','r')
    T = int(fin.readline())
        
    #Start calculation:    
    fout = open('outputFrac.txt','w')
        
    for t in range(T):
        K, C, S = fin.readline().strip().split(' ')
        K, C, S = int(K), int(C), int(S)
        
        placement = ''
        if C*S < K:
            fout.write('Case #' + str(t+1) + ': ' + 'IMPOSSIBLE\n')
            continue;
            
        Kdone = 0
        offset = 0
        count = 1
        while K+offset < C:
            offset += 1
        for i in range(1,C):
            if (C-i-1-offset) < 0:
                break
            count += (Kdone+i)*K**(C-i-1-offset)
        placement += str(count) + ' '
        Kdone += C -offset
        
        while Kdone < K:
            offset = 0
            while K-Kdone+offset < C:
                offset += 1
            
            count = 1
            for i in range(C-offset):
                count += (Kdone+i)*K**(C-i-1-offset)
            placement += str(count) + ' '
            Kdone += C - offset
        

        placement = placement.strip()
        if len(placement.split(' ')) > S:
            placement = 'IMPOSSIBLE'
        fout.write('Case #' + str(t+1) + ': ' + placement + '\n')
    
    fin.close() 
    fout.close()
    print 'done'
    
    
    
    
    