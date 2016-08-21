
# coding: utf-8

# In[141]:

def solve(pancakes):
    cpt = 0
    taille = len(pancakes)
    i = 0
    flip = False
    while(i<taille):
        if(pancakes[i]=='-' and flip==False):
            flip = True
            if('+' in pancakes[:i]):
                cpt+=2
            else:
                cpt+=1
        if(pancakes[i]=='+'):
            if(flip == True):
                flip = False
        i+=1
    return cpt


# In[142]:

f = open('B-small-attempt0.in', 'r')
res = open('res.B', 'w')


# In[143]:

n_lines = int(f.readline().strip())


# In[144]:

num_line = 1
for line in f:
    line = line.strip()
    cpt = solve(line)
    res.writelines("Case #"+str(num_line)+": "+str(cpt)+"\n")
    num_line +=1


# In[145]:

f.close()
res.close()

