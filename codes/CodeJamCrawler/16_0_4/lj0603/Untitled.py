
# coding: utf-8

# In[10]:

infile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\4\\D-small-attempt1.in', 'r')
outfile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\4\\result.txt', 'w')
N=int(infile.readline())
for i in range(N):
    x=infile.readline()
    index_blank_1=0
    for j in range(4):
        if x[j]==' ':
            index_blank_1=j
            break
    index_blank_2=index_blank_1+1
    for j in range(index_blank_1+1,index_blank_1+5):
        if x[j]==' ':
            index_blank_2=j
            break
    k=int(x[0:index_blank_1])
    c=int(x[index_blank_1+1:index_blank_2])
    outfile.write('case #'+str(i+1)+':')
    for j in range(k):
        outfile.write(' '+str(1+j*k**(c-1)))
    outfile.write('\n')
infile.close()
outfile.close()


# In[ ]:



