
# coding: utf-8

# In[30]:

IN = 'A-large.in.txt'
OUT = 'A-small-1-attempt0.txt'
with open(IN) as f:
    fin = iter(f.readlines())
    
    data = []
    
    allnum = [0,0,0,0,0,0,0,0,0,0]
    ncases = int(next(fin).strip())
    for i in range(ncases):
        n = int(next(fin).strip())
        allnum = [0,0,0,0,0,0,0,0,0,0]
        for gogo in range(1,3000000):
            nowN=gogo*n
            strn=str(nowN)
            for wa in range(len(strn)):
                if(allnum[int(strn[wa])]==0):
                    allnum[int(strn[wa])]=1
                    #print allnum
            if (allnum ==[1,1,1,1,1,1,1,1,1,1]):
                print 'Case #%s: %d' % (i+1, nowN)
                data.append('Case #%s: %d' % (i+1, nowN)) 
                break
            elif (gogo==2999999):
                print 'Case #%s: %s' % (i+1, "INSOMNIA")
                data.append('Case #%s: %s' % (i+1, "INSOMNIA"))
                break
with open(OUT, 'wb') as ff:
    ff.write('\n'.join(data) + '\n')


# In[ ]:



