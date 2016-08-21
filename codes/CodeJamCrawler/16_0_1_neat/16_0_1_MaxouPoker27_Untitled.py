
# coding: utf-8

# In[43]:

def solve(num):
    nombres = set()
    if(num == 0):
        return "INSOMNIA"
    coef = 0
    value = 0
    while(len(nombres)!=10):
        coef+=1
        value=coef*num
        for v in str(value):
            nombres.add(v)
        value = int(value)
    return value


# In[44]:

f = open('test.in', 'r')
res = open('res.B', 'w')


# In[45]:

n_lines = int(f.readline().strip())


# In[46]:

num_line = 1
for line in f:
    line = line.strip()
    cpt = solve(int(line))
    res.writelines("Case #"+str(num_line)+": "+str(cpt)+"\n")
    num_line +=1


# In[47]:

f.close()
res.close()

