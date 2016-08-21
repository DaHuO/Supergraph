
# coding: utf-8

# In[12]:

def flip_pancake(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')
    
    for i in range(T):
        pancake = fr.readline().strip()
        j = 0
        
        idx_p = pancake.find('+')
        idx_n = pancake.find('-')
        while idx_n != -1:
            if idx_p == -1:
                j += 1
                break
                
            j += 1
            if idx_p < idx_n:
                pancake = idx_n*'-' + pancake[idx_n:]
            else:
                pancake = idx_p*'+' + pancake[idx_p:]
                
            idx_p = pancake.find('+')
            idx_n = pancake.find('-')
            
        
        fw.write('Case #%d: %d\n'%(i+1, j))
        
    fr.close()
    fw.close()


# In[15]:

flip_pancake('B-large.in')


# In[ ]:



