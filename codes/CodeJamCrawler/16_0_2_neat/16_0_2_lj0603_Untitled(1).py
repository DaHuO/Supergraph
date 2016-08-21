
# coding: utf-8

# In[3]:

infile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\2\\B-small-attempt2.in', 'r')
outfile = open('C:\\Users\\liujun0603\\Desktop\\core\\comp\\google\\2016\\2\\result.txt', 'w')
def handle(series):
    series.reverse()
    for s in range(len(series)):
        if series[s]=='+':
            series[s]='-'
        else:
            series[s]='+'
    return series
N=int(infile.readline())
for i in range(N):
    print('case'+str(i))
    series=infile.readline()
    series=list(series)
    del series[-1]
    series.reverse()
    length=len(series)
    n=0
    for j in range(0,length-1):
        if series[j]=='+':
            continue
        else:
            if series[length-1]=='-':
                series[j:length]=handle(series[j:length])
                n+=1
                print(series)
                print(n)
            else:
                for k in reversed(range(j,length)):
                    print(series[k])
                    if series[k]=='+':
                        series[k]='-'
                    else:
                        break
                series[j:length]=handle(series[j:length])
                n+=2
                print(series)
                print(n)
    if series[length-1]=='-':
        n+=1
    print(series)
    outfile.write('case #'+str(i+1)+': '+str(n)+'\n')
infile.close()
outfile.close()


# In[ ]:




# In[ ]:



