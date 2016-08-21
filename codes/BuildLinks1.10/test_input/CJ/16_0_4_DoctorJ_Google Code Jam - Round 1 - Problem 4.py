
# coding: utf-8

# In[1]:

f = open('input.in','r')
o = open('OutP4.out','w')
nTests = int(f.readline())
for i in range (1,nTests+1):
    K,C,S = [int(x) for x in f.readline().split()]
    
    if (C==1):
        if S<K:
            result = 'IMPOSSIBLE'
        else:
            result = list(range(1,K+1))
    else:
        if S<(K-1):
            result = 'IMPOSSIBLE'
        else:
            if K == 1:
                result = list('1')
            else:
                result = list(range(2,K+1))

    if result == 'IMPOSSIBLE':
        o.write("Case #"+str(i)+": "+str(result)+"\n")
    else:
        o.write("Case #"+str(i)+":")
        for text in result:
            o.write(" "+str(text))
        o.write("\n")
        
o.close()
f.close()


# In[ ]:



