# import numpy as np

if __name__ == '__main__':
    
    fin = open('A-large.in','r')
    fout = open('output.txt','w')
    
    T = int(fin.readline())
    names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    
    #Start calculation:    
    for t in range(T):
        N = int(fin.readline())
        tot = 0
        P = fin.readline().strip().split(' ')
        for i in range(N):
            P[i] = int(P[i])
            tot += P[i]
        P_sorted = sorted(P)
        
        
        evac = ''
        
        leader = P.index(P_sorted[-1])
        opposition = P.index(P_sorted[-2])
        if opposition==leader:
            for i in range(N):
                if i==leader:
                    continue
                if P[i] == P[leader]:
                    opposition = i
                    break
        
        while (P[leader] > P[opposition]):
            evac += min(min(2,P[leader]),P[leader]-P[opposition])*(names[leader]) + ' '
            P[leader] -= min(min(2,P[leader]),P[leader]-P[opposition])
        
        for i in range(N):
            if (i==leader or i==opposition):
                continue
            while (P[i]>0):
                evac += min(2,P[i])*(names[i]) + ' '
                P[i] -= min(2,P[i])
        
        evac += P[leader]*(names[leader]+names[opposition] + ' ')
        
    
        fout.write('Case #' + str(t+1) + ': ' + evac.strip() + '\n')
    
    
    
    fin.close()
     
    fout.close()
    print 'done'
    