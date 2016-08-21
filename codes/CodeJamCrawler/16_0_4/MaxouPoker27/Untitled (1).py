
# coding: utf-8

# In[37]:

def solve(num):
    s=""
    for i in range(1,num+1):
        s+=str(i)+" "
    return s.strip()


# In[38]:

f = open('D-small-attempt0.in', 'r')
res = open('res.C', 'w')


# In[39]:

n_lines = int(f.readline().strip())


# In[40]:

for num_line, line in enumerate(f):
    line = line.strip()
    line = line.split(' ')
    cpt = solve(int(line[2]))
    res.writelines("Case #"+str(num_line+1)+": "+str(cpt)+"\n")


# In[41]:

f.close()
res.close()

