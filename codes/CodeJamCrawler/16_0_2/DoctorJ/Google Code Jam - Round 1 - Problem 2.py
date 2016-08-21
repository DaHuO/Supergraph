
# coding: utf-8

# In[1]:

def reduceString (cStr):
    newStr = list(cStr[0])
    for i in range(1,len(cStr)):
        if cStr[i]!=cStr[i-1]:
            newStr.append(cStr[i])
    return newStr


# In[2]:

f = open('input.in','r')
o = open('OutP2.out','w')
nTests = int(f.readline())
for i in range(1,nTests+1):
    qq = reduceString(f.readline())
    qq.reverse()
    if '-' in qq:
        result = len(qq) - qq.index('-')
    else:
        result = 0
    o.write("Case #"+str(i)+": "+str(result)+"\n")
f.close()
o.close()

