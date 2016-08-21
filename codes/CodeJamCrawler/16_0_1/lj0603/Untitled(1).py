
# coding: utf-8

# In[33]:

infile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\1\\A-small-attempt1.in', 'r')
outfile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\1\\result.txt', 'w')
N=int(infile.readline())
print(N)
for i in range(N):
    x=infile.readline()
    n=int(x)
    compset=set('0123456789')
    series=set(str(n))
    for j in range(1,100):
        current=n*j
        series=series|set(str(current))
        print(current)
        print(series)
        if series==compset:
            outfile.write('case #'+str(i+1)+': '+str(current)+'\n')
            break
        else:
            continue
    else:
        outfile.write('case #'+str(i+1)+': '+'INSOMNIA'+'\n')
infile.close()
outfile.close()


# In[ ]:




# In[ ]:



