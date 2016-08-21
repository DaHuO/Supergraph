
# coding: utf-8

# In[129]:

def solve(N):
    if digits(N) == set() or 0 == N:
        return "INSOMNIA"
    
    return until(N)


# In[62]:

def digits(i):
    ds = set()
    while i != 0:
        ds.add(i % 10)
        i = i / 10
    return ds


# In[127]:

def until(n):
    nc = n
    current = 1
    ds = digits(nc)
    while ds != set([0,1,2,3,4,5,6,7,8,9]):
        current += 1
        nc = current * n
        ds = ds.union(digits(nc))
        if current == 200:
            raise Exception("Bug!")
    
    return nc


# In[126]:

digits(1234567890)


# In[131]:

path = r'E:\Downloads\A-small-attempt0.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        N = int(f.readline())
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(N)))

