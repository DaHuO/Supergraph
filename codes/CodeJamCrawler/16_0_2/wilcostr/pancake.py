# import numpy as np

if __name__ == '__main__':
    
    fin = open('B-large.in','r')
    T = int(fin.readline())
    
    
    #Start calculation:    
    fout = open('output.txt','w')
        
    for t in range(T):
        cakes = fin.readline().strip()
        l = len(cakes)
        count = 0
        vis = cakes[0]
        for i in range(1,l):
            if cakes[i] != vis:
                count += 1
                vis = '+' if vis=='-' else '-'
        
        if vis=='-':
            count += 1
            
#         print cakes, count
        fout.write('Case #' + str(t+1) + ': ' + str(count) + '\n')
     
    fin.close()
    fout.close()
    print 'done'