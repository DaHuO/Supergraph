
# coding: utf-8

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[12]:

def solve(word):
    res = ''
    for w in word:
        if not res or w < res[0]:
            res += w
        else:
            res = w + res
    
    return res
    
        


# In[ ]:




# In[14]:

path = r'E:\Downloads\A-small-attempt0.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        word = f.readline().rstrip()
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(word)))

