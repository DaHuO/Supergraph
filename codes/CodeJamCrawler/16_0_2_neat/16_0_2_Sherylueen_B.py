
# coding: utf-8

# In[1]:

def Section(intPancake):
    section = 1
    comp = intPancake[0]
    for pp in range(1,len(intPancake)):
        if comp != intPancake[pp]:
            section += 1
            comp = intPancake[pp]
    return section
caseNum = int(raw_input())
for i in range(caseNum):
    intPancake = []
    pancake = raw_input()
    last = len(intPancake)-1
    for j in pancake:
        if j == '+':
            intPancake.append(1)
        else:
            intPancake.append(0)
    if intPancake[last]:
        res = Section(intPancake) - 1
    else:
        res = Section(intPancake)
    print 'Case #'+str(i + 1)+': '+str(res)
            
            


# In[ ]:



