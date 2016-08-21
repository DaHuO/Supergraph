
# coding: utf-8

# In[58]:

def count_sheep(file_in):
    fr = open(file_in, 'r')
    T = int(fr.readline().strip())
    fw = open(file_in[:-3] + '.out', 'w')
    for i in range(T):
        N = int(fr.readline().strip())
        if N == 0:
#             print('Case #%d: INSOMNIA'%(i+1))
            fw.write('Case #%d: INSOMNIA\n'%(i+1))
        else:
            M = N
            count = set(list(str(M)))
            while len(count) != 10:
                M += N
                count.update(list(str(M)))
#             print('Case #%d: %d'%(i+1,M))
            fw.write('Case #%d: %d\n'%(i+1,M))
    fr.close()
    fw.close()


# In[59]:

count_sheep('A-large.in')


# In[ ]:



