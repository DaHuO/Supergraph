
# coding: utf-8

# In[31]:


def solve(pancakes):
    flips = 0
    index = 0
    
    current = '+'
    for index in xrange(len(pancakes)):
        print index, pancakes[index], current
        if pancakes[index] == current:
            continue
        flips = flips + 1
        current = '-' if current == '+' else '+'
        
    if flips == 0:
        return 0
    
    if pancakes[0] == '+':
        flips += 1
        
    if pancakes[index] == '+':
        flips -= 1
    
    return flips


# In[ ]:




# In[ ]:




# In[ ]:




# In[33]:

path = r'E:\Downloads\B-small-attempt0.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        pancakes = f.readline().rstrip()
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(pancakes)))

