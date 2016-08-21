
# coding: utf-8

# In[7]:

from collections import defaultdict


# In[49]:

x =["THREE", "NINE"]
sorted(''.join(x))


# In[80]:

def solve(s):
    #print s
    c = defaultdict(lambda: 0)
    
    sol = ''
    
    for let in s:
        c[let] += 1
    
    numbers = [("ZERO", 'Z'), ("TWO", 'W'), ("SIX", 'X') ,("FOUR", 'U'),("ONE", 'O'),("SEVEN", 'S'), ("EIGHT", 'G'), ("FIVE", 'V'),("THREE", 'T'),("NINE", 'I')]
    numbers_sorted = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for i,num_iden in enumerate(numbers):
        num = num_iden[0]
        iden = num_iden[1]
        
        while True:
            #print iden, c[iden]
            if 0 == c[iden]:
                break
                
            sol += str(numbers_sorted.index(num))
            for let in num:
                c[let] -= 1
    
    #print sol, c
    for l in c:
        assert not c[l]
    
    return ''.join(sorted(sol))


# In[ ]:




# In[81]:

solve("OZONETOWER")


# In[82]:

path = r'E:\Downloads\A-small-attempt3.in'
with open(path, 'r') as f, open(path[:-2]+'out', 'w') as outf:
    T = int(f.readline())
    for test_index in xrange(T):
        s = f.readline().rstrip()
        outf.write('Case #{}: {}\n'.format(test_index+1, solve(s)))

